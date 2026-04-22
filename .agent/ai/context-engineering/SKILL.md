# Context Engineering Skills

> **Framework de Context Engineering para agentes IA**

Integração dos skills de [muratcankoylan/agent-skills-for-context-engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering).

## 🎯 O que é Context Engineering?

Context engineering é a disciplina de **gerenciar a janela de contexto** do modelo de linguagem:

| Problema | Solução |
|---------|---------|
| Lost-in-the-middle | Chunking inteligente |
| Attention scarcity | Progressive disclosure |
| U-shaped attention | High-signal tokens first |
| Context poisoning | Filtros de qualidade |

## 🔧 Skills Core

### Context Fundamentals
```
Use quando: Entender como contexto afeta performance
```

### Context Degradation
```
Use quando: Diagnosticar problemas de contexto
Trigger: "debug agent", "fix hallucinations"
```

### Context Compression
```
Use quando: Reduzir tokens sem perder signal
Trigger: "compress context", "summarize"
```

## 📊 Progressive Disclosure Pattern

### Nível 1: Meta (carrega primeiro)
```markdown
# Skill: nome
description: quando usar
```

### Nível 2: Full (ativa quando necessário)
```markdown
# Skill: nome (extended)
## Workflow completo
## Exemplos
## Trade-offs
```

### Nível 3: Data (só se requerido)
```markdown
# Skill: nome (data)
## Referências
## Scripts
```

## 🧠 Memory Architecture

### Short-term (in-session)
- Last N messages
- Tool outputs recentes
- Current task state

### Long-term (cross-session)
- ChromaDB embeddings
- Custom fixes
- Project context

### Graph-based (entidades)
- Relacionamentos
- Entity tracking
- Cross-reference

## 🔗 Integração com Antigravity

| Antigravity | Context Engineering |
|-----------|-------------------|
| `agent_router.py` | Context routing patterns |
| `chroma_db/` | Memory architecture |
| `knowledge_distiller.py` | Context distillation |
| `monitor.py` | Observabilidade |

---

**Origem:** [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | **Stars:** 15.2k ⭐