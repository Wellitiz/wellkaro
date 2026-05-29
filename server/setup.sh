#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
# setup.sh — Compilar e configurar rAthena na VPS Ubuntu
# ═══════════════════════════════════════════════════════════════════
set -e

echo "══════════════════════════════════════════════"
echo "  WellkaRO — Setup do Servidor rAthena"
echo "══════════════════════════════════════════════"

# 1. Instalar dependências de compilação
echo "[1/5] Instalando dependências..."
sudo apt update
sudo apt install -y git make gcc g++ zlib1g-dev libmysqlclient-dev \
    libpcre3-dev libssl-dev mysql-server mysql-client \
    nginx certbot python3-certbot-nginx nodejs npm python3-pip python3-venv

# 2. Instalar PM2
echo "[2/5] Instalando PM2..."
sudo npm install -g pm2

# 3. Clonar o rAthena (versão oficial)
echo "[3/5] Clonando rAthena..."
if [ ! -d "/home/ubuntu/rathena" ]; then
    git clone https://github.com/rathena/rathena.git /home/ubuntu/rathena
fi

# 4. Compilar o rAthena
echo "[4/5] Compilando rAthena..."
cd /home/ubuntu/rathena
./configure --enable-packetver=20211103
make clean
make server

# 5. Copiar configurações customizadas
echo "[5/5] Aplicando configurações do WellkaRO..."
cp -r /home/ubuntu/wellkaro/server/conf/import/* /home/ubuntu/rathena/conf/import/

echo ""
echo "══════════════════════════════════════════════"
echo "  ✅ rAthena compilado com sucesso!"
echo "  Próximo passo: configurar o banco de dados"
echo "  Execute: mysql -u root -p < /home/ubuntu/wellkaro/server/sql-files/main.sql"
echo "══════════════════════════════════════════════"
