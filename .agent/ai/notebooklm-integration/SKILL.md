# NotebookLM Integration

> **Integração com Google NotebookLM para RAG source-grounded**

## 🎯 O que é

O NotebookLM é o knowledge base do Google alimentado por Gemini 2.5 que fornece respostas **exclusivamente** de seus documentos carregados.

## 📊 Comparação RAG

| Abordagem | Custo Tokens | Setup | Alucinações | Qualidade |
|-----------|-------------|-------|-------------|-----------|
| Feed docs to Claude | 🔴 Alto | Instant | Sim | Variável |
| Local RAG | 🟡 Médio | Horas | Médio | Depende |
| **NotebookLM** | 🟢 Baixo | 5 min | **Mínimo** | Expert synthesis |

## 🔌 Integração Antigravity

### Arquitetura
```
Usuário → Antigravity → NotebookLM API → Resposta source-grounded
```

### Casos de Uso

1. **Documentação técnica** → Upload manuais → Pergunte sobre especificações
2. **Código legado** → Index notebooks → Pergunte sobre padrões
3. **Regras de negócio** → Documentação KI → Chat contextual

## 📋 Comandos

### Query NotebookLM
```
"Ask my [nome] notebook about [tópico]"
```

### Adicionar Notebook
```
"Add this notebook to my library: [url]"
```

### Listar Notebooks
```
"Show my NotebookLM notebooks"
```

## ⚠️ Requisitos

- Google account com acesso ao NotebookLM
- Notebooks compartilhados publicamente
- Rate limits no tier free

## 🔗 Integração com Antigravity

| Componente | Papel |
|-----------|-------|
| `chroma_db/` | RAG local (backup) |
| `knowledge_distiller.py` | Distilla respostas |
| `agent_router.py` | Routing inteligente |

## 📝 Exemplo Prático

**Task:** "Check my React docs about hooks"

**Sem NotebookLM:**
1. Carrega múltiplos arquivos
2. Token overhead alto
3. Resposta variável

**Com NotebookLM:**
1. Query direta ao notebook
2. Tokens mínimos
3. Resposta source-grounded

---

**Origem:** [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) | **Stars:** 6k ⭐