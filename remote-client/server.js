const express = require("express");
const path = require("path");
const fs = require("fs");
const { GrfNode, fixMojibake } = require("@chicowall/grf-loader");

const app = express();
const PORT = process.env.PORT || 3338;
const DATA_DIR = path.join(__dirname, "data");

// Array to hold our GRF loaders
let grfs = [];

// Load GRF files asynchronously
async function loadGRFs() {
  const grfFiles = ["coresnovas.grf", "data.grf"];
  for (const file of grfFiles) {
    const filePath = path.join(DATA_DIR, file);
    if (fs.existsSync(filePath)) {
      try {
        const fd = fs.openSync(filePath, "r");
        const grfInstance = new GrfNode(fd, { maxFiles: 1500000, maxEntries: 1500000 });
        await grfInstance.load();
        grfs.push({ name: file, instance: grfInstance });
        console.log(`[RemoteClient] Successfully loaded GRF archive: ${file} (total files: ${grfInstance.files.size})`);
      } catch (err) {
        console.error(`[RemoteClient] Error loading GRF archive ${file}:`, err.message);
      }
    } else {
      console.warn(`[RemoteClient] ⚠️ GRF file not found: ${filePath}`);
    }
  }
}

loadGRFs().catch((err) => {
  console.error("[RemoteClient] Fatal error loading GRFs:", err);
});

// CORS to allow requests from roBrowser
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "GET, OPTIONS");
  res.header("Access-Control-Allow-Headers", "Content-Type");
  next();
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

// Wildcard asset server route
app.get("/*", async (req, res) => {
  const reqPath = req.params[0];
  if (!reqPath) {
    return res.status(404).send("File not found");
  }

  // Normalize path: decode URL, convert forward slashes to backslashes
  let assetPath = decodeURIComponent(reqPath).replace(/\//g, "\\");

  // Fix Mojibake encoding issues (original casing preserved!)
  let fixedPath = fixMojibake(assetPath);

  // For GRF lookup, make sure it has the "data\" prefix
  let grfPath = fixedPath;
  if (!grfPath.toLowerCase().startsWith("data\\")) {
    grfPath = "data\\" + grfPath;
  }

  // Search in loaded GRFs (coresnovas first, then data)
  for (let grf of grfs) {
    try {
      // Resolve path case-insensitively and slash-agnostically
      const resolved = grf.instance.resolvePath(grfPath);
      if (resolved && resolved.status === "found" && resolved.matchedPath) {
        const result = await grf.instance.getFile(resolved.matchedPath);
        if (result && result.data) {
          const fileData = Buffer.from(result.data);
          
          // Determine content type
          const ext = path.extname(resolved.matchedPath).toLowerCase();
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
      }
    } catch (err) {
      console.error(`[RemoteClient] Error reading ${grfPath} from ${grf.name}:`, err.message);
    }
  }

  // Fallback to static directory if file is extracted on disk
  const diskPath = path.join(DATA_DIR, reqPath);
  if (fs.existsSync(diskPath) && fs.statSync(diskPath).isFile()) {
    return res.sendFile(diskPath);
  }

  console.log(`[RemoteClient] 404 - Asset not found in GRFs or disk: ${fixedPath} (original: ${reqPath})`);
  res.status(404).send("File not found");
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`[RemoteClient] Server listening on http://0.0.0.0:${PORT}`);
});


