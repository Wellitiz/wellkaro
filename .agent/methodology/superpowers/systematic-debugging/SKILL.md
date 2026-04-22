# Systematic Debugging

> **Debug em 4 fases para root cause analysis**

Use quando bugs são reportados ou tests falham.

## 🔄 Processo de Debug

### Fase 1: Isolar
- Reproduza o bug consistentemente
- Crie teste falhando
- Determine input exato que causa falha

### Fase 2: Hipóteses
- Liste possíveis causas
- Priorize por likelihood
- Documente cada hipótese

### Fase 3: Testar
- Teste hipótese mais provável
- Se não, tente próxima
- Documente descobertas

### Fase 4: Corrigir
- Aplique correção mínima
- Execute testes
- Verifique que problema foi resolvido
- Documente correção

## 🔧 Técnicas de Espera Condicional

### poll()
```python
for i in range(50):
    result = api.get_status()
    if result == 'ready':
        return result
    time.sleep(0.1)
```

### wait_for()
```python
def wait_for(predicate, timeout=30):
    start = time.time()
    while time.time() - start < timeout:
        if predicate():
            return True
        time.sleep(0.1)
    raise TimeoutError()
```

## ⚠️ Defense in Depth

Camadas de proteção contra falhas:
- Input validation
- Error boundaries
- Fallbacks
- Retry logic

## 🔗 Skills Relacionados

- `@test-driven-development` - TDD após debug
- `@verification-before-completion` - verificar fix

---

**Origem:** [obra/superpowers](https://github.com/obra/superpowers)