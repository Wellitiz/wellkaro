# Writing Plans Skill

> **Criar planos de implementação detalhados**

Use quando o design está aprovado e você precisa de um plano de execução.

## 🎯 Quando Ativar

- Design foi aprovado pelo usuário
- Task requer múltiplos passos
- Usuário diz "vá", "execute", "implemente"

## 📋 Estrutura do Plano

Cada task deve:
- Ter **2-5 minutos** de duração
- Ter **caminhos de arquivo exatos**
- Ter **código completo** (não pseudocódigo)
- Ter **passos de verificação**

## 📝 Template

```markdown
# Plano: [Nome da Feature]

## Tasks

### Task 1: [Nome Descortivo]
**Duração:** ~2-5 min
**Arquivos:** 
- `src/feature/task1.ts` (criar)
- `src/types.ts` (modificar)

**Código:**
```typescript
// Código completo aqui
```

**Verificação:**
```bash
npm test src/feature/task1.test.ts
```

### Task 2: [Nome Descortivo]
...
```

## ⚠️ Princípios YAGNI

- **You Aren't Gonna Need It**
- Só adicione código/features que são necessários agora
- Evite over-engineering
- Refatore quando necessário, não antes

## ⚠️ Regras DRY

- **Don't Repeat Yourself**
- Código duplicado = código frágil
- Extraia para funções/componentes reutilizáveis

## 🔗 Skills Relacionados

- `@brainstorming` - Antes deste skill
- `@subagent-driven-development` - Após este skill
- `@test-driven-development` - Durante execução

---

**Origem:** [obra/superpowers](https://github.com/obra/superpowers)