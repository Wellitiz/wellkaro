const express = require("express");
const path = require("path");
const fs = require("fs");
const { GrfNode } = require("@chicowall/grf-loader");

const app = express();
const PORT = process.env.PORT || 3338;
const DATA_DIR = path.join(__dirname, "data");

// Array to hold our GRF loaders
let grfs = [];

// Load GRF files
function loadGRFs() {
  const grfFiles = ["coresnovas.grf", "data.grf"];
  grfFiles.forEach((file) => {
    const filePath = path.join(DATA_DIR, file);
    if (fs.existsSync(filePath)) {
      try {
        const fd = fs.openSync(filePath, "r");
        const grfInstance = new GrfNode(fd);
        grfs.push({ name: file, instance: grfInstance });
        console.log(`[RemoteClient] Successfully loaded GRF archive: ${file}`);
      } catch (err) {
        console.error(`[RemoteClient] Error loading GRF archive ${file}:`, err.message);
      }
    } else {
      console.warn(`[RemoteClient] ⚠️ GRF file not found: ${filePath}`);
    }
  });
}

loadGRFs();

// CORS to allow requests from roBrowser
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "GET, OPTIONS");
  res.header("Access-Control-Allow-Headers", "Content-Type");
  next();
});

// Serve assets from GRFs dynamically
app.get("/data/*", (req, res) => {
  // Extract requested asset path relative to /data/
  let assetPath = req.params[0];
  
  // Normalize path: decode URL, convert slashes to backslashes (GRF standard)
  assetPath = decodeURIComponent(assetPath).replace(/\//g, "\\").toLowerCase();

  // Search in loaded GRFs (coresnovas first, then data)
  for (let grf of grfs) {
    try {
      const fileEntry = grf.instance.getFile(assetPath);
      if (fileEntry) {
        const fileData = grf.instance.getFileContent(fileEntry);
        
        // Determine content type
        const ext = path.extname(assetPath).toLowerCase();
        let contentType = "application/octet-stream";
        if (ext === ".bmp") contentType = "image/bmp";
        else if (ext === ".png") contentType = "image/png";
        else if (ext === ".xml") contentType = "application/xml";
        else if (ext === ".txt") contentType = "text/plain";
        else if (ext === ".wav") contentType = "audio/wav";
        else if (ext === ".mp3") contentType = "audio/mpeg";

        res.setHeader("Content-Type", contentType);
        res.setHeader("Cache-Control", "public, max-age=2592000, immutable"); // 30 days cache
        return res.send(fileData);
      }
    } catch (err) {
      console.error(`[RemoteClient] Error reading ${assetPath} from ${grf.name}:`, err.message);
    }
  }

  // Fallback to static directory if file is extracted on disk
  const diskPath = path.join(DATA_DIR, req.params[0]);
  if (fs.existsSync(diskPath) && fs.statSync(diskPath).isFile()) {
    return res.sendFile(diskPath);
  }

  console.log(`[RemoteClient] 404 - Asset not found in GRFs or disk: ${assetPath}`);
  res.status(404).send("File not found");
});

// Health check
app.get("/health", (req, res) => {
  res.json({
    status: "ok",
    service: "remote-client",
    loadedGRFs: grfs.map((g) => g.name),
  });
});

app.get("/", (req, res) => {
  res.json({
    service: "WellkaRO Remote Client",
    version: "1.0.0",
    loadedGRFs: grfs.map((g) => g.name),
    message: "Use /data/{path} to access game assets directly from GRFs",
  });
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`[RemoteClient] Server listening on http://0.0.0.0:${PORT}`);
});
