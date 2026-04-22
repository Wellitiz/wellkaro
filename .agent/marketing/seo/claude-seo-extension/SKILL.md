# CLAUDE SEO EXTENSION - Advanced Layer

> **Extensões avançadas do Claude SEO para o Antigravity**

Este skill integra as funcionalidades avançadas do [claude-seo](https://github.com/AgriciDaniel/claude-seo) ao Antigravity v5.

## 🎯 Diferença para Skills Existentes

O Antigravity já tem `seo-fundamentals`, `seo-technical`, etc. Este layer adiciona:

| Já Existente | Este Layer Adiciona |
|-------------|-------------------|
| SEO básico | Google APIs (PageSpeed, CrUX, GSC) |
| Schema simples | Video schema, Live schema |
| SEO padrão | GEO/AEO (AI Search Optimization) |
| SEM Google | Google Search Console API |
| Backlinks free | DataForSEO extensões |

## 🔌 Comandos Avançados

### `/seo google report [tipo]`

Gera relatórios PDF com gráficos via WeasyPrint:

```
/seo google report cwv-audit      # Core Web Vitals audit
/seo google report gsc-performance  # GSC organic traffic
/seo google report full         # Relatório completo
```

### `/seo geo [url]`

Otimiza para AI Search (Google AI Overviews, ChatGPT, Perplexity):

```
/seo geo https://example.com      # Análise GEO
/seo geo优化             # GEO (simplified)
/seo geo https://example.com/blog  # Blog optimization
```

### `/seo drift [comando]`

Monitora mudanças SEO ao longo do tempo:

```
/seo drift baseline https://example.com   # Captura baseline
/seo drift compare https://example.com  # Compara com baseline
/seo drift history https://example.com  # Histórico
```

## 📊 Google APIs Integration

### Configuração (4 tiers)

| Tier | APIs Disponíveis |
|------|--------------|
| 0 | PageSpeed Insights, CrUX |
| 1 | + GSC, URL Inspection, Indexing |
| 2 | + GA4 organic traffic |
| 3 | + Keyword Planner |

### Setup

```bash
# Obter credenciais em:
//console.cloud.google.com

# Variáveis de ambiente
GOOGLE_API_KEY=...
GOOGLE_SEARCH_CONSOLE_KEY=...
GA4_PROPERTY_ID=...
```

## 📋 Schema Types Avançados

### VideoObject
```json
{
  "type": "VideoObject",
  "description": "Tutorial completo",
  "thumbnailUrl": "https://...",
  "duration": "PT10M30S",
  "uploadDate": "2026-04-21"
}
```

### BroadcastEvent (Live)
```json
{
  "type": "BroadcastEvent",
  "isLiveNow": true,
  "startDate": "2026-04-21T20:00:00Z"
}
```

### Clip (Capítulos)
```json
{
  "type": "Clip",
  "name": "Introdução",
  "startOffset": "PT0M0S",
  "endOffset": "PT2M30S"
}
```

## 🎯 Quando Usar

- **Análise avançada** → `/seo google [comando]`
- **Otimização AI** → `/seo geo [url]`
- **Monitoramento** → `/seo drift [comando]`
- **Relatórios PDF** → `/seo google report full`

## 🔗 Skills Relacionados

- `@seo-fundamentals` - base
- `@seo-technical` - audits
- `@seo-content` - conteúdo

---

**Origem:** [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | **Stars:** 5.3k ⭐