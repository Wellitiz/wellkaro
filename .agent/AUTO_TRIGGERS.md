# 🎯 Auto-Triggers: Comandos Automáticos do Antigravity v5.1

> Este arquivo mapeia trigger words → skills automaticamente ativadas

## 📋 Quick Reference

| Quando você digita... | O Antigravity automaticamente ativa... |
|----------------------|----------------------------------|
| "construir" | `@brainstorming` → pergunta sobre design |
| "criar um sistema" | `@brainstorming` + `@writing-plans` |
| "teste primeiro" | `@test-driven-development` |
| "tem um bug" | `@systematic-debugging` |
| "otimizar conversão" | `@marketing-skills-extension` (CRO) |
| "otimizar landing page" | `@marketing-skills-extension` |
| "SEO" ou "google" | `@claude-seo-extension` |
| "/seo" | `@claude-seo-extension` |
| "relatório SEO" | `/seo google report full` |
| "AI search" | `/seo geo [url]` |
| "drift" | `/seo drift compare [url]` |
| "copywriting" | Copywriting (AIDA/PAS frameworks) |
| "cold email" | Cold email template |
| "sequência de email" | Email sequence |
| "teste A/B" | A/B Testing framework |
| "vídeo" | `@remotion` |
| "/remotion" | Remotion development |
| "reduzir tokens" | `@context-engineering` |
| "compress" | Context compression |
| "pergunte aos docs" | NotebookLM integration |
| "notebook" | NotebookLM queries |
| "review código" | `@requesting-code-review` |
| "terminar feature" | `@finishing-a-development-branch` |
| "subir para o git" | `git_sync.py` → Sincroniza Core v5.1 |

---

## 🔄 Automatic Triggers (Sem Comando)

### Superpowers (Workflow)
```
"preciso construir [algo]" → brainstorming + plans + execution
"vou desenvolver" → subagent-driven-development
"primeiro o teste" → test-driven-development
"preciso debugar" → systematic-debugging
"terminou?" → finishing-branch
"revisao" → code-review
"git worktree" → using-git-worktrees
```

### Marketing (CRO/SEO)
```
"landing page" → page-cro
"conversões" → conversion optimization
"formulário" → form-cro
"signup" → signup-flow-cro
"copy" → copywriting (AIDA)
"email" → cold-email / email-sequence
"blog post" → seo-content
"SEO audit" → seo-technical
"Google" → google-apis
"PageSpeed" → google-pagespeed
"tráfego" → gsc-performance
```

### AI/Context
```
"memória" → context memory
"context" → context-engineering
"chunk" → context-compression
"lost in middle" → context-degradation
"hallucination" → notebooklm (source-grounded)
"docs" → notebooklm query
"pergunte sobre" → notebooklm query
```

### Frontend
```
"vídeo" → remotion
"animação" → remotion
"render" → remotion
"template video" → remotion templates
```

---

## 🎯 Como Funciona

O `agent_router.py` busca no `chroma_db` porsimilaridade semântica. Este arquivo contém as trigger words para que o sistema reconheça automaticamente quando você mencionar esses conceitos.

**Zero configuração necessária** - o sistema já faz isso automaticamente.

---

## 📊 Mapeamento Completo

| Categoria | Trigger | Skill Arquivo |
|-----------|---------|---------------|
| Workflow | build, criar, construir | `.methodology/superpowers/brainstorming/` |
| Workflow | plano, implementation | `.methodology/superpowers/writing-plans/` |
| Workflow | execute, rodar | `.methodology/superpowers/subagent-driven-development/` |
| Workflow | teste, TDD | `.methodology/superpowers/test-driven-development/` |
| Workflow | debug, bug | `.methodology/superpowers/systematic-debugging/` |
| Workflow | review, revise | `.methodology/superpowers/requesting-code-review/` |
| Workflow | merge, finish | `.methodology/superpowers/finishing-a-development-branch/` |
| Marketing | conversion, CRO, otimize | `.marketing/marketing-skills-extension/` |
| Marketing | SEO, google | `.marketing/seo/claude-seo-extension/` |
| Marketing | copy, escritura | `.marketing/marketing-skills-extension/` |
| Marketing | email, cold | `.marketing/marketing-skills-extension/` |
| AI | context, memória | `.ai/context-engineering/` |
| AI | notebook, docs | `.ai/notebooklm-integration/` |
| Front | video, animacao | `.frontend/remotion/` |

---

> 💡 **Dica:** Não precisa digitar comandos. Só fale naturalmente!
> "Preciso criar uma landing page que Converts" → O sistema entende e ativa CRO automaticamente.