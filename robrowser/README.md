# roBrowser — Cliente Web

Este diretório contém o cliente web roBrowserLegacy.

## Setup

1. Clone o roBrowserLegacy:
   ```bash
   git clone https://github.com/nicBrowser/roBrowserLegacy.git /tmp/robrowser
   ```

2. Copie os arquivos necessários:
   ```bash
   cp -r /tmp/robrowser/dist/js /home/ubuntu/wellkaro/robrowser/js
   cp -r /tmp/robrowser/dist/AI /home/ubuntu/wellkaro/robrowser/AI
   ```

3. O `index.html` já está configurado com as conexões corretas.

## Configuração

Edite o `ROConfig` em `index.html` para ajustar:
- `address`: URL do wsProxy (WebSocket)
- `remoteClient`: URL do RemoteClient (assets)
- `packetver`: Versão do pacote (deve coincidir com o servidor)
