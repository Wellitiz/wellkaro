# 🚀 Guia Universal: Deploy Next.js na Hostinger

Este guia define as configurações obrigatórias para qualquer projeto Next.js hospedado na Hostinger via Painel (hPanel) ou VPS simples.

---

## 1. Banco de Dados (Ambientes Compartilhados)
Se o Banco de Dados MySQL e o Site estão na mesma conta Hostinger, a conexão **DEVE** ser via IP Local.
- **DATABASE_URL**: `mysql://usuario:senha@127.0.0.1:3306/nome_banco`
- *Nota: O host `mysql.hostinger.com` é apenas para conexões externas (seu PC local).*

## 2. Protocolo de Redirecionamento (Auth)
A maioria dos provedores de Autenticação (NextAuth, Clerk, Auth.js) exige o protocolo completo.
- **Protocolo**: Sempre incluir `https://` no início das URLs.
- **Exemplo**: `NEXTAUTH_URL=https://meudominio.com`

## 3. Script de Correção de Permissões (Linux)
Ao subir arquivos do Windows para o Linux da Hostinger, pastas como `[id]` perdem permissão de leitura. Adicione ao seu `package.json`:
```json
"scripts": {
  "prebuild": "chmod -R 755 src || exit 0"
}
```

## 4. Preset Next.js vs Standalone
- Se utilizar o **Configuração Predefinida: Next.js** do hPanel: **NÃO** utilize `output: 'standalone'` no `next.config`.
- Envie apenas os arquivos de origem (`src`, `public`, `prisma`, `package.json`, etc.).
- O Hostinger fará o `npm install` e `npm build` automaticamente.

## 5. Limpeza do Pacote (Zip)
Nunca envie `node_modules` ou a pasta `.next` de desenvolvimento local. Isso causa erros de versão de binários (Sharp, Prisma, etc.) entre Windows e Linux.

---
*Assinado: Antigravity Kit Protocol*
