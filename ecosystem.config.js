module.exports = {
  apps: [
    // ═══════════════════════════════════════════════
    // 1. wsProxy — WebSocket ↔ TCP bridge
    // ═══════════════════════════════════════════════
    {
      name: "wsproxy",
      script: "index.js",
      cwd: "/home/ubuntu/wellkaro/wsproxy",
      env: {
        NODE_ENV: "production",
      },
      restart_delay: 3000,
      max_restarts: 10,
    },

    // ═══════════════════════════════════════════════
    // 2. RemoteClient — Serve assets GRF via HTTP
    // ═══════════════════════════════════════════════
    {
      name: "remote-client",
      script: "server.js",
      cwd: "/home/ubuntu/wellkaro/remote-client",
      env: {
        NODE_ENV: "production",
        PORT: 3338,
      },
      restart_delay: 3000,
      max_restarts: 10,
    },

    // ═══════════════════════════════════════════════
    // 3. Painel GM — Flask app
    // ═══════════════════════════════════════════════
    {
      name: "gm-panel",
      script: "app.py",
      cwd: "/home/ubuntu/wellkaro/gm",
      interpreter: "/home/ubuntu/wellkaro/gm/venv/bin/python",
      env: {
        FLASK_ENV: "production",
      },
      restart_delay: 3000,
      max_restarts: 10,
    },
  ],
};
