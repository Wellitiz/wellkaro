# Brainstorming Skill

> **Design colaborativo antes de escrever código**

Use quando o usuário menciona uma tarefa de desenvolvimento que requer design ou arquitetura.

## 🎯 Quando Ativar

- Usuário quer construir algo novo
- Task envolve múltiplos componentes
- Requer decisões de design/arquitetura
- Usuário menciona "construir", "criar", "implementar", "desenhar"

## 🔄 Fluxo de Ativação

### Fase 1: Esclarecer o Problema

1. **Pergunte o que realmente quer fazer**
2. Explore alternativas e trade-offs
3. Documente constraints

### Fase 2: Design Incremental

1. Apresente design em **chunks pequenos**
2. Valide cada chunk antes de continuar
3. Itere baseado em feedback

### Fase 3: Salvar Design

1. Salve design documentado
2. Defina próxima ação clara

## 💡 Técnicas Socráticas

Em vez de assumir, pergunte:

```
"Você quer que [feature X] funcione offline também?"
"O que acontece se [edge case Y] ocorrer?"
"Existe alguma limitação técnica que devo conhecer?"
"Qual é mais importante: [A] ou [B]?"
```

## 📝 Template de Design

```markdown
# Design: [Nome da Feature]

## Problema
[O que o usuário quer resolver]

## Solução Proposta
[Descrição de alto nível]

## Decisões de Design
1. [Decisão 1] - [Rationale]
2. [Decisão 2] - [Rationale]

## Próxima Ação
[O que fazer agora]
```

## ⚠️ Regras

- ❌ **Não** pule para código
- ❌ **Não** assuma decisões de design
- ✅ **Pergunte** clarificações
- ✅ **Apresente** em chunks pequenos
- ✅ **Valide** antes de continuar

## 🔗 Skills Relacionados

- `@writing-plans` - Após design aprovado
- `@using-git-worktrees` - Setup do workspace
- `@subagent-driven-development` - Execução do plano

---

**Origem:** [obra/superpowers](https://github.com/obra/superpowers)