# Finishing a Development Branch

> **Merge/PR decision workflow**

Use quando todas as tasks estão completas.

## 🎯 Quando Ativar

- Todas as tasks do plano completas
- Code review aprobado
- Testes passando

## 🔄 Opções de Finalização

### Opção 1: Merge
```bash
git checkout main
git merge feature/my-feature
```

### Opção 2: Pull Request
```bash
git push origin feature/my-feature
# Criar PR via GitHub/GitLab UI
```

### Opção 3: Manter Branch
```bash
git branch -D feature/my-feature  # local
git push origin --delete feature/my-feature  # remote
```

## 📋 Checklist Before Merge

- [ ] Todos os testes passando
- [ ] Code review aprobado
- [ ] Documentação atualizada
- [ ] CHANGELOG.md atualizado
- [ ] Nenhum merge conflict

## ⚠️ Limpeza do Worktree

```bash
# Se usou worktree, remova após merge
git worktree remove feature-my-feature
```

## 🔗 Skills Relacionados

- `@requesting-code-review` - antes de finalizar
- `@subagent-driven-development` - workflow completo

---

**Origem:** [obra/superpowers](https://github.com/obra/superpowers)