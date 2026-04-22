# Subagent-Driven Development

> **Execução via subagentes com revisão em duas etapas**

Use quando o plano está pronto e você pode paralelizar tarefas.

## 🎯 Quando Ativar

- Plano de implementação existe
- Múltiplas tasks independentes
- Usuário disse "vá" ou "execute"

## 🔄 Workflow

```
1. Dispare subagente por task
2. Revisão Fase 1: Compliance com spec
3. Revisão Fase 2: Qualidade do código
4. Repita ou avance
```

## 📋 Revisão em Duas Etapas

### Fase 1: Spec Compliance
- ✅ Task foi completada?
- ✅ Todos os arquivos criados?
- ✅ Testes passando?

### Fase 2: Code Quality
- ✅ Sem código duplicado?
- ✅ Nomenclatura consistente?
- ✅ Comments onde necessário?

## ⚠️ Padrão RED-GREEN-REFACTOR

**SEMPRE** antes de escrever código de produção:

1. **RED** - Escreva teste falhando
2. **GREEN** - Código mínimo passando
3. **REFACTOR** - Limpe código

## 🔗 Skills Relacionados

- `@writing-plans` - Antes deste skill
- `@test-driven-development` - TDD durante execução
- `@requesting-code-review` - Após completar tasks
- `@finishing-a-development-branch` - Finalização

---

**Origem:** [obra/superpowers](https://github.com/obra/superpowers)