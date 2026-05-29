/**
 * ═══════════════════════════════════════════════════════════════════
 * WellkaRO — Remote Client (Asset Server)
 * ═══════════════════════════════════════════════════════════════════
 *
 * Serve os assets do data.grf via HTTP para o roBrowser.
 * O roBrowser requisita sprites, mapas, texturas etc. via HTTP
 * e este servidor extrai do arquivo .grf em tempo real.
 *
 * Porta: 3338
 *
 * IMPORTANTE:
 *   O arquivo data.grf (~4.5GB) deve ser enviado via SCP/rsync
 *   para /home/ubuntu/wellkaro/remote-client/data/
 */

const express = require("express");
const path = require("path");
const fs = require("fs");

const app = express();
const PORT = process.env.PORT || 3338;

// Diretório onde os assets extraídos/data.grf ficam
const DATA_DIR = path.join(__dirname, "data");

// CORS para permitir requisições do roBrowser
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "GET, OPTIONS");
  res.header("Access-Control-Allow-Headers", "Content-Type");
  next();
});

// Serve arquivos estáticos da pasta data/
app.use("/data", express.static(DATA_DIR, {
  maxAge: "30d",
  immutable: true,
}));

// Health check
app.get("/health", (req, res) => {
  res.json({ status: "ok", service: "remote-client", dataDir: DATA_DIR });
});

// Fallback — lista arquivos disponíveis (debug)
app.get("/", (req, res) => {
  res.json({
    service: "WellkaRO Remote Client",
    version: "1.0.0",
    dataDir: DATA_DIR,
    message: "Use /data/{path} para acessar assets do jogo",
  });
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`[RemoteClient] Serving assets on http://0.0.0.0:${PORT}`);
  console.log(`[RemoteClient] Data directory: ${DATA_DIR}`);

  // Verifica se o diretório de dados existe
  if (!fs.existsSync(DATA_DIR)) {
    console.warn(`[RemoteClient] ⚠️  Data directory not found: ${DATA_DIR}`);
    console.warn(`[RemoteClient]    Crie a pasta e envie os assets via SCP.`);
    fs.mkdirSync(DATA_DIR, { recursive: true });
  }
});
