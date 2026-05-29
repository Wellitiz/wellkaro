/**
 * ═══════════════════════════════════════════════════════════════════
 * WellkaRO — wsProxy (WebSocket → TCP Bridge)
 * ═══════════════════════════════════════════════════════════════════
 *
 * Este serviço recebe conexões WebSocket do roBrowser (navegador)
 * e as redireciona para o servidor rAthena via TCP.
 *
 * Portas:
 *   - WebSocket: 5999 (entrada do navegador)
 *   - TCP saída: 6900 (login), 6121 (char), 5121 (map)
 *
 * Protocolo:
 *   O primeiro pacote do cliente contém o IP:porta do servidor
 *   de destino. O wsProxy abre uma conexão TCP e faz o relay
 *   bidirecional de pacotes.
 */

const WebSocket = require("ws");
const net = require("net");

const WS_PORT = process.env.WS_PORT || 5999;

// Endereço do servidor rAthena (localhost na mesma VPS)
const RATHENA_HOST = process.env.RATHENA_HOST || "127.0.0.1";

// Portas do rAthena
const PORTS = {
  login: 6900,
  char: 6121,
  map: 5121,
};

const wss = new WebSocket.Server({ port: WS_PORT });

console.log(`[wsProxy] Listening on ws://0.0.0.0:${WS_PORT}`);
console.log(`[wsProxy] Forwarding to ${RATHENA_HOST}:${PORTS.login}/${PORTS.char}/${PORTS.map}`);

wss.on("connection", (ws, req) => {
  const clientIP = req.headers["x-forwarded-for"] || req.socket.remoteAddress;
  console.log(`[wsProxy] New connection from ${clientIP}`);

  let tcpSocket = null;
  let targetPort = PORTS.login; // Default: login server
  let isFirstPacket = true;

  ws.on("message", (data) => {
    // Se é o primeiro pacote, pode conter informação de destino
    if (isFirstPacket) {
      isFirstPacket = false;

      // Tenta extrair porta de destino do header customizado do roBrowser
      // O roBrowser envia: [2 bytes port][rest of packet]
      if (data.length >= 2) {
        const port = data.readUInt16LE(0);
        if (port === PORTS.login || port === PORTS.char || port === PORTS.map) {
          targetPort = port;
          data = data.slice(2); // Remove o header de porta
        }
      }

      // Abre conexão TCP com o rAthena
      tcpSocket = net.createConnection({ host: RATHENA_HOST, port: targetPort }, () => {
        console.log(`[wsProxy] TCP connected to ${RATHENA_HOST}:${targetPort}`);
        if (data.length > 0) {
          tcpSocket.write(data);
        }
      });

      tcpSocket.on("data", (tcpData) => {
        if (ws.readyState === WebSocket.OPEN) {
          ws.send(tcpData);
        }
      });

      tcpSocket.on("close", () => {
        console.log(`[wsProxy] TCP connection closed (${targetPort})`);
        if (ws.readyState === WebSocket.OPEN) {
          ws.close();
        }
      });

      tcpSocket.on("error", (err) => {
        console.error(`[wsProxy] TCP error: ${err.message}`);
        if (ws.readyState === WebSocket.OPEN) {
          ws.close();
        }
      });

      return;
    }

    // Relay: WebSocket → TCP
    if (tcpSocket && !tcpSocket.destroyed) {
      tcpSocket.write(data);
    }
  });

  ws.on("close", () => {
    console.log(`[wsProxy] WebSocket closed (${clientIP})`);
    if (tcpSocket && !tcpSocket.destroyed) {
      tcpSocket.destroy();
    }
  });

  ws.on("error", (err) => {
    console.error(`[wsProxy] WebSocket error: ${err.message}`);
    if (tcpSocket && !tcpSocket.destroyed) {
      tcpSocket.destroy();
    }
  });
});
