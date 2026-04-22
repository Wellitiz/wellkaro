# Test-Driven Development (TDD)

> **RED-GREEN-REFACTOR cycle**

Use quando escrevendo código de produção.

## 🔄 Ciclo TDD

### RED: Escreva teste falhando
```typescript
test('deve retornar soma', () => {
  expect(add(2, 3)).toBe(5);
});
// Execute → FAIL ✗
```

### GREEN: Código mínimo passando
```typescript
function add(a: number, b: number) {
  return a + b;
}
// Execute → PASS ✓
```

### REFACTOR: Limpe código
- Remova duplicação
- Melhore nomenclatura
- Extraia funções quando necessário
- Execute testes após cada mudança

## ⚠️ Anti-Patterns

| ❌ Evite | ✅ Use |
|---------|-------|
| Código antes do teste | Teste primeiro |
| Testes vagos | Testes específicos |
| 100% coverage | Coverage significativo |
| TDD em UI simples | TDD em lógica de negócio |

## 📋 Quando NÃO usar TDD

- Exploratory coding
- Scripts simples
- UI estática
- Configuração

## 📋 Quando SIM usar TDD

- Lógica de negócio
- APIs
- Transformações de dados
- Cálculos

## 🔗 Skills Relacionados

- `@subagent-driven-development` - workflow pai
- `@systematic-debugging` - debug de testes falhando

---

**Origem:** [obra/superpowers](https://github.com/obra/superpowers)