# Painel GM

Este diretório contém o painel administrativo do servidor WellkaRO.
O painel GM já foi enviado anteriormente para a VPS.

## Acesso

- URL: `https://wellkaro.wellka.com.br/gm`
- Backend: Flask (Python) rodando na porta 5000

## Setup na VPS

```bash
cd /home/ubuntu/wellkaro/gm
python3 -m venv venv
source venv/bin/activate
pip install flask mysql-connector-python
```
