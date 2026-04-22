# Superpowers Methodology - AI Agent Workflow System

> **Um framework completo de metodologia de desenvolvimento agentic**

O Superpowers é uma metodologia de desenvolvimento de software que transforma agentes de IA em desenvolvedores eficazes seguindo workflows estruturados.

## 🧠 O que é Superpowers?

O Superpowers começa no momento em que você ativa o agente de codificação. Quando ele percebe que você está construindo algo, ele **não** pula para escrever código. Em vez disso:

1. **Recua e pergunta** o que você realmente quer fazer
2. **Refina o design** através de perguntas socráticas
3. **Mostra o plano em chunks** curtos o suficiente para ler
4. **Cria um plano de implementação** claro
5. **Executa via subagentes** com revisão em duas etapas

## 🔄 Workflow Principal

```
brainstorming → using-git-worktrees → writing-plans → subagent-driven-development → code-review → finishing-branch
```

### Skills Disponíveis

| Skill | Função |
|-------|-------|
| `brainstorming` | Design colaborativo antes de codar |
| `using-git-worktrees` | Branching isolado para cada feature |
| `writing-plans` | Planos de implementação detalhados |
| `subagent-driven-development` | Execução via subagentes paralelos |
| `test-driven-development` | RED-GREEN-REFACTOR cycle |
| `systematic-debugging` | Debug em 4 fases |
| `requesting-code-review` | Review estruturado |
| `finishing-a-development-branch` | Merge/PR decision workflow |

## 🎯 Quando Usar

- **Qualquer task de desenvolvimento novo** → Começa com `brainstorming`
- **Tasks complexas** → Usa `writing-plans` + `subagent-driven-development`
- **Bug fixing** → Usa `systematic-debugging`
- **Antes de commitar** → Usa `requesting-code-review`

## 📁 Estrutura

```
methodology/superpowers/
├── SKILL.md (este arquivo)
├── brainstorming/
│   └── SKILL.md
├── using-git-worktrees/
│   └── SKILL.md
├── writing-plans/
│   └── SKILL.md
├── subagent-driven-development/
│   └── SKILL.md
├── test-driven-development/
│   └── SKILL.md
├── systematic-debugging/
│   └── SKILL.md
├── requesting-code-review/
│   └── SKILL.md
└── finishing-a-development-branch/
    └── SKILL.md
```

## 🔗 Integração com Antigravity

O Antigravity já tem:
- `agent_router.py` - Orquestrador neural
- `knowledge_distiller.py` - Aprendizado autônomo

O Superpowers complementa com **workflows estruturados** antes de cada task.

---

**Origem:** [obra/superpowers](https://github.com/obra/superpowers) | **Stars:** 163k ⭐