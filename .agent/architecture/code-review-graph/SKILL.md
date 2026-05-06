# Skill: Code Review Graph (Structural Context)

> **Mapeamento Estrutural e Análise de Raio de Impacto.**

## 🎯 O que é
Esta skill integra o `code-review-graph` ao core do Antigravity. Ela transforma o código-fonte em um grafo de conhecimento persistente, permitindo que o agente entenda dependências, chamadores e fluxos lógicos que a busca vetorial (RAG) comum ignora.

## 🛠️ Funcionalidades Mestre

1.  **Blast Radius Analysis**: Identifica quais arquivos e funções serão afetados por uma mudança.
2.  **Structural RAG**: Fornece contexto preciso baseado na hierarquia de chamadas, não apenas em palavras-chave.
3.  **Token Efficiency**: Reduz o uso de tokens ao ler apenas o que é estruturalmente relevante.

## 🔌 Integração no Core (v6.5)

### Gatilhos Automáticos
O Antigravity ativa o `code-review-graph` sempre que:
- Um novo repositório é indexado.
- Uma tarefa de "refatoração" ou "bug fix" é solicitada.
- O comando `python git_sync.py` é executado (para atualizar o grafo antes do push).

### Comandos Principais
- `code-review-graph build`: Reconstrói o mapa do projeto.
- `code-review-graph detect-changes`: Analisa o risco das mudanças atuais.
- `code-review-graph visualize`: Gera uma visão macro da arquitetura.

## 📜 Regras de Consciência
- **Fato sobre Semântica**: Em conflitos de arquitetura, o Grafo Estrutural tem prioridade sobre a Busca Vetorial.
- **Auto-Update**: O grafo deve ser atualizado (`update`) após cada bloco significativo de edições.

---
**Origem:** [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | **Categoria:** Arquitetura / Inteligência
