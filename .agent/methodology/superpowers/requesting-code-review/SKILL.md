# Requesting Code Review

> **Review estruturado antes de merge**

Use entre tasks ou antes de finalizar branch.

## 🎯 Quando Ativar

- Task completa
- Antes de merge/PR
- Entre fases do plano

## 🔄 Checklist de Review

### Compliance Check
- [ ] Feature funcionando como especificado?
- [ ] Testes passando?
- [ ] Edge cases tratados?
- [ ] Documentação atualizada?

### Code Quality Check
- [ ] Sem código duplicado?
- [ ] Nomenclatura consistente?
- [ ] Comments onde necessário?
- [ ] Sem código commented-out?
- [ ] Error handling presente?

### Security Check
- [ ] Input validation?
- [ ] SQL injection protected?
- [ ] XSS protected?
- [ ] Secrets not in code?

## 📋 Report Template

```markdown
## Code Review: [Branch/Feature]

### ✅ Aprovado
- [ ] items approve

### ⚠️ Issues Leves
- [ ] suggestions opcionais

### 🔴 Issues Bloqueantes
- [ ] critical issues

### 📝 Comentários
[Detailed comments]
```

## ⚠️ Prioridades

| Prioridade | Impacto | Ação |
|-----------|--------|------|
| 🔴 Critical | Bloqueia merge | Corrigir antes |
| ⚠️ Moderate | Nice to fix | Pode ser deferred |
| 💡 Suggestion | Melhoria | Próxima sprint |

## 🔗 Skills Relacionados

- `@subagent-driven-development` - após tasks
- `@finishing-a-development-branch` - finalização

---

**Origem:** [obra/superpowers](https://github.com/obra/superpowers)