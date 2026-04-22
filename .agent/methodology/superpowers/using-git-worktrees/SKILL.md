# Using Git Worktrees

> **Branching isolado para desenvolvimento paralelo**

Use para criar workspaces isolados por feature.

## 🎯 Quando Ativar

- Task nova de desenvolvimento
- Antes de começar implementation
- Worktree disponível no repo

## 🔄 Workflow

```bash
# 1. Criar worktree para feature
git worktree add -b feature/my-feature ../feature-my-feature

# 2. Trabalhar no worktree isolado
cd ../feature-my-feature

# 3. Commitar mudanças
git add .
git commit -m "feat: my feature"

# 4. Voltar ao main
cd ..
git checkout main

# 5. Merge ou deletar worktree
git worktree remove feature-my-feature
```

## ✅ Benefícios

- **Isolamento** - cada feature em workspace separado
- **Paralelismo** - múltiplas features simultâneas
- **Zero conflitos** - branches nunca se misturam
- **Limpeza** - fácil deletar worktrees abandonadas

## ⚠️ Quando NÃO usar

- Hotfixes pequenos
- Changes de documentação
- Tasks de 5 minutos

## ⚠️ Quando SIM usar

- Features grandes
- Refactors complexos
- experimentação
- Multiple tarefas simultâneas

## 🔗 Skills Relacionados

- `@brainstorming` - antes de criar worktree
- `@finishing-a-development-branch` - após completar

---

**Origem:** [obra/superpowers](https://github.com/obra/superpowers)