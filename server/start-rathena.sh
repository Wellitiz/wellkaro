#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
# start-rathena.sh — Iniciar os servidores rAthena via PM2
# ═══════════════════════════════════════════════════════════════════

RATHENA_DIR="/home/ubuntu/rathena"

echo "Iniciando servidores rAthena..."

# Login Server (porta 6900)
cd $RATHENA_DIR
pm2 start ./login-server --name "rathena-login" -- --run-once

# Char Server (porta 6121)
pm2 start ./char-server --name "rathena-char" -- --run-once

# Map Server (porta 5121)
pm2 start ./map-server --name "rathena-map" -- --run-once

# Web Server (rAthena built-in)
pm2 start ./web-server --name "rathena-web" -- --run-once

echo "✅ Todos os servidores rAthena iniciados!"
echo "Use 'pm2 status' para verificar."
