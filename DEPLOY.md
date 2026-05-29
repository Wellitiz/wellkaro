# 🚀 WellkaRO — Guia Completo de Deploy na VPS

Este guia assume uma VPS Oracle (Ubuntu) com o domínio `wellkaro.wellka.com.br` já apontando para o IP da VPS.

---

## 📋 Pré-requisitos

- VPS Ubuntu 20.04+ (Oracle Cloud, 4 vCPU / 24GB RAM)
- Domínio `wellkaro.wellka.com.br` com registro A apontando para o IP da VPS
- Acesso SSH à VPS (`ssh ubuntu@SEU_IP_VPS`)

---

## 🛠️ Passo 1 — Instalar Dependências

```bash
# Conectar à VPS
ssh ubuntu@SEU_IP_VPS

# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar tudo de uma vez
sudo apt install -y git make gcc g++ zlib1g-dev libmysqlclient-dev \
    libpcre3-dev libssl-dev mysql-server mysql-client \
    nginx certbot python3-certbot-nginx nodejs npm python3-pip python3-venv

# Instalar PM2 globalmente
sudo npm install -g pm2
```

---

## 📁 Passo 2 — Clonar o Repositório

```bash
cd /home/ubuntu

# Se a pasta wellkaro já existe (com o gm-panel), faça backup
# mv wellkaro wellkaro-backup

# Clonar o repositório
git clone https://github.com/Wellitiz/wellkaro.git

# Se tinha backup do gm, copie de volta
# cp -r wellkaro-backup/gm/* wellkaro/gm/
```

---

## 🗄️ Passo 3 — Configurar o Banco de Dados (MySQL)

```bash
# Acessar o MySQL como root
sudo mysql

# Dentro do MySQL, executar:
CREATE DATABASE ragnarok;
CREATE USER 'wellkaro'@'localhost' IDENTIFIED BY 'SUA_SENHA_FORTE_AQUI';
GRANT ALL PRIVILEGES ON ragnarok.* TO 'wellkaro'@'localhost';
FLUSH PRIVILEGES;
EXIT;

# Importar as tabelas do rAthena
mysql -u wellkaro -p ragnarok < /home/ubuntu/wellkaro/server/sql-files/main.sql
mysql -u wellkaro -p ragnarok < /home/ubuntu/wellkaro/server/sql-files/logs.sql
mysql -u wellkaro -p ragnarok < /home/ubuntu/wellkaro/server/sql-files/web.sql

# Criar conta de admin (GM)
mysql -u wellkaro -p ragnarok -e "INSERT INTO login (account_id, userid, user_pass, sex, group_id) VALUES (2000000, 'admin', 'admin', 'M', 99);"
```

> ⚠️ **IMPORTANTE:** Substitua `SUA_SENHA_FORTE_AQUI` por uma senha real e segura.

---

## ⚔️ Passo 4 — Compilar o rAthena

O servidor rAthena precisa ser compilado para Linux (os .exe são Windows):

```bash
# Clonar o rAthena oficial
git clone https://github.com/rathena/rathena.git /home/ubuntu/wellkaro/rathena

# Entrar na pasta
cd /home/ubuntu/wellkaro/rathena

# Configurar e compilar
./configure --enable-packetver=20211103
make clean
make server

# Copiar as configurações customizadas do WellkaRO
cp /home/ubuntu/wellkaro/server/conf/import/* /home/ubuntu/wellkaro/rathena/conf/import/
```

### Editar as configurações com o IP da VPS:

```bash
# Substituir SEU_IP_VPS_AQUI pelo IP real da VPS em todos os configs
IP_VPS="SEU_IP_AQUI"

sed -i "s/SEU_IP_VPS_AQUI/$IP_VPS/g" /home/ubuntu/wellkaro/rathena/conf/import/char_conf.txt
sed -i "s/SEU_IP_VPS_AQUI/$IP_VPS/g" /home/ubuntu/wellkaro/rathena/conf/import/map_conf.txt
sed -i "s/SEU_IP_VPS_AQUI/$IP_VPS/g" /home/ubuntu/wellkaro/rathena/conf/import/login_conf.txt

# Substituir a senha do banco
sed -i "s/SUA_SENHA_AQUI/SUA_SENHA_FORTE_AQUI/g" /home/ubuntu/wellkaro/rathena/conf/import/inter_conf.txt
```

---

## 🌐 Passo 5 — Configurar o roBrowser (Cliente Web)

```bash
# Clonar o roBrowserLegacy
git clone https://github.com/nicBrowser/roBrowserLegacy.git /tmp/robrowser

# Copiar os arquivos do roBrowser para a pasta do projeto
cp -r /tmp/robrowser/dist/js /home/ubuntu/wellkaro/robrowser/js
cp -r /tmp/robrowser/dist/AI /home/ubuntu/wellkaro/robrowser/AI

# Verificar se o index.html está correto
cat /home/ubuntu/wellkaro/robrowser/index.html
```

---

## 📦 Passo 6 — Instalar dependências Node.js

```bash
# wsProxy
cd /home/ubuntu/wellkaro/wsproxy
npm install

# Remote Client
cd /home/ubuntu/wellkaro/remote-client
npm install
```

---

## 📂 Passo 7 — Enviar os Assets do Jogo (data.grf)

Os arquivos `.grf` são muito grandes para o Git (~4.5GB). Envie via SCP:

```bash
# Do seu PC Windows (PowerShell/Terminal):
scp "C:\Users\welli\Downloads\Ragnarok\Client 2025 RuneHost\Client 2025 RuneHost\data.grf" ubuntu@SEU_IP_VPS:/home/ubuntu/wellkaro/remote-client/data/

scp "C:\Users\welli\Downloads\Ragnarok\Client 2025 RuneHost\Client 2025 RuneHost\coresnovas.grf" ubuntu@SEU_IP_VPS:/home/ubuntu/wellkaro/remote-client/data/
```

> ⏳ Isso pode demorar bastante (~4.5GB). Considere usar `rsync` para retomar em caso de queda.

---

## 🔧 Passo 8 — Configurar o Nginx

```bash
# Copiar a configuração do Nginx
sudo cp /home/ubuntu/wellkaro/nginx/wellkaro.conf /etc/nginx/sites-available/wellkaro

# Ativar o site
sudo ln -s /etc/nginx/sites-available/wellkaro /etc/nginx/sites-enabled/

# Testar a configuração
sudo nginx -t

# Recarregar
sudo systemctl reload nginx

# Obter certificado SSL (HTTPS)
sudo certbot --nginx -d wellkaro.wellka.com.br
```

---

## 🚀 Passo 9 — Iniciar Todos os Serviços

### A. Painel GM (Flask):
```bash
cd /home/ubuntu/wellkaro/gm
python3 -m venv venv
source venv/bin/activate
pip install flask mysql-connector-python
deactivate
```

### B. Iniciar rAthena:
```bash
cd /home/ubuntu/wellkaro/rathena
pm2 start ./login-server --name "rathena-login"
pm2 start ./char-server --name "rathena-char"
pm2 start ./map-server --name "rathena-map"
```

### C. Iniciar serviços Node.js e GM:
```bash
cd /home/ubuntu/wellkaro
pm2 start ecosystem.config.js
```

### D. Salvar e configurar auto-start:
```bash
pm2 save
pm2 startup
# Execute o comando que o PM2 sugerir (com sudo)
```

---

## 🔒 Passo 10 — Liberar Portas no Firewall

### Oracle Cloud (Console Web):
1. Vá em **Virtual Cloud Networks** → sua VCN → **Security Lists**
2. Adicione **Ingress Rules**:
   - Source CIDR: `0.0.0.0/0`, Protocol: `TCP`, Port: `80`
   - Source CIDR: `0.0.0.0/0`, Protocol: `TCP`, Port: `443`

### Na VPS:
```bash
sudo iptables -I INPUT 6 -p tcp --dport 80 -j ACCEPT
sudo iptables -I INPUT 6 -p tcp --dport 443 -j ACCEPT
sudo netfilter-persistent save
```

---

## ✅ Passo 11 — Verificar

| Teste | Comando/URL |
|-------|-------------|
| rAthena rodando | `pm2 status` |
| Cliente web | `https://wellkaro.wellka.com.br` |
| Painel GM | `https://wellkaro.wellka.com.br/gm` |
| wsProxy | `pm2 logs wsproxy` |
| RemoteClient | `curl http://localhost:3338/health` |

---

## 🔄 Atualizações Futuras

```bash
cd /home/ubuntu/wellkaro
git pull origin main
pm2 restart all
```

---

## ⚠️ Troubleshooting

| Problema | Solução |
|----------|---------|
| `nginx -t` falha | Verifique sintaxe em `/etc/nginx/sites-available/wellkaro` |
| rAthena não conecta ao MySQL | Verifique senha em `conf/import/inter_conf.txt` |
| Cliente web não carrega | Verifique se o roBrowser JS está em `robrowser/js/` |
| WebSocket não conecta | Verifique `pm2 logs wsproxy` e firewall |
| Assets não carregam | Verifique se `data.grf` está em `remote-client/data/` |
| Painel GM inacessível | Verifique `pm2 logs gm-panel` e rota Nginx `/gm` |
