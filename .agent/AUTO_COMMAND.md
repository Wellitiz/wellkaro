# 🎯 Auto-Execute Slash Command

> **Use `/auto` para executar comandos automáticos**

## Uso

No seu prompt do Antigravity, basta usar:

```
/auto make a video
```

ou

```
/auto run SEO audit on https://example.com
```

## Comandos Disponíveis

| Comando | Ação |
|---------|------|
| `/auto make a video` | Cria projeto Remotion |
| `/auto run SEO audit [url]` | Executa audit SEO |
| `/auto run google report` | Gera relatório PDF |
| `/auto build video` | Compila vídeo Remotion |
| `/auto dev` | Inicia servidor Remotion |

## Exemplos

```
/auto make a video for my product launch
/auto run SEO audit on https://mysite.com
/auto build video
```

## Como Funciona

1. Você digita `/auto [comando]`
2. O sistema extrai o comando
3. Executa automaticamente via `auto_executor_cli.py`
4. Retorna o resultado

---

**Nota:** O sistema também detecta automaticamente via busca semântica,
mas `/auto` força a execução imediata.