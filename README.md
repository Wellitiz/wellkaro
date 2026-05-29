# WellkaRO — Servidor Ragnarok Online (Zero-Download)

Servidor Ragnarok Online com cliente web acessível via navegador.

## Arquitetura

```
Navegador (roBrowser) ──WebSocket──▶ wsProxy (porta 5999) ──TCP──▶ rAthena (porta 6900/6121/5121)
                                        │
                                   RemoteClient (porta 3338) ◀── Serve assets do data.grf
```

## Estrutura do Repositório

```
wellkaro/
├── server/           # Configurações do rAthena (conf, sql-files, npc, db)
│   ├── conf/         # Arquivos de configuração do servidor
│   ├── sql-files/    # Scripts SQL para criar o banco de dados
│   └── setup.sh      # Script de compilação do rAthena no Linux
├── wsproxy/          # WebSocket Proxy (Node.js) — ponte browser↔servidor
├── robrowser/        # Cliente web roBrowserLegacy (HTML/JS)
├── remote-client/    # Servidor de assets GRF (Node.js)
├── gm/               # Painel administrativo GM (Flask/Python)
├── nginx/            # Configurações prontas do Nginx
└── ecosystem.config.js  # PM2 — gerenciamento de processos
```

## Domínios

| Serviço | URL |
|---------|-----|
| Cliente Web (jogo) | `https://wellkaro.wellka.com.br` |
| Painel GM | `https://wellkaro.wellka.com.br/gm` |

## Guia de Deploy

Consulte o [DEPLOY.md](./DEPLOY.md) para instruções passo-a-passo.
