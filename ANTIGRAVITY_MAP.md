# 🛸 Antigravity v6.5 Structural Consciousness: Mapa do Ecossistema

Este documento fornece a visualização estrutural completa do ecossistema Antigravity, detalhando a função de cada camada e arquivo no sistema.

---

## 🗺️ Mapa Arquitetural (Project Tree)

```text
ANTIGRAVITY_ROOT/
├── 🧠 Intelligence & RAG Core ( O Coração )
│   ├── agent_router.py       # Orquestrador v6 (Multi-Agent Team Debate)
│   ├── index_skills.py       # Motor de Indexação Híbrida v4
│   ├── skill_generator.py    # Universal Expansion (GitHub Import)
│   ├── auto_rag.py           # Planejador Automático (Context Builder)
│   ├── auto_executor.py      # Autonomous Bridge
│   ├── run.py                 # Ponto de Entrada Universal
│   └── monitor.py             # Monitor de Consciência Real-time
│
├── 📂 Knowledge Base ( Memória Global )
│   ├── .agent/               # Repositório de 1.300+ Agentes e Skills
│   │   ├── ai/               # Modelos, Prompts e Especialistas em LLM
│   │   │   ├── context-agent/       # Context management
│   │   │   └── notebooklm-integration/ # NotebookLM RAG integration
│   │   ├── frontend/         # React, Next.js, UI/UX, CSS, Tailwind
│   │   │   ├── remotion/    # Video generation via React
│   │   │   └── pretext/     # High-performance text layout [v6.2]
│   │   ├── design/           # Design Intelligence (Pentagon of Perfection)
│   │   │   ├── impeccable/   # AI Design Language
│   │   │   ├── huashu-design/# Advanced Prototyping
│   │   │   ├── ui-ux-pro-max/# Multi-platform UI/UX
│   │   │   └── taste-skill/  # Anti-slop guardian
│   │   ├── architecture/     # System design and code mapping
│   │   │   └── code-review-graph/ # Knowledge Graph [v6.5]
│   │   ├── automation/       # Autonomous Action & Testing
│   │   │   └── playwright/   # Browser automation [v7.0 base]
│   │   ├── backend/          # Node, Python, Databases, APIs
│   │   ├── security/         # Auditoria, Auth, Proteção, Pentest
│   │   ├── marketing/        # SEO, Content, CRO, Copywriting
│   │   │   ├── seo/              # SEO fundamentals + extensions
│   │   │   ├── seo/claude-seo-extension/  # Google APIs, GEO
│   │   │   └── marketing-skills-extension/  # CRO, Email, Analytics
│   │   ├── methodology/      # Workflow systems
│   │   │   └── superpowers/  # Superpowers agentic workflow
│   │   └── ... (mais 50+ categorias multitag)
│   └── chroma_db/            # Banco Vetorial (HNSW Index v5)
│
├── 🔄 Learning Loop ( Consciência v6.0 )
│   ├── knowledge_distiller.py # Destilador de Memória
│   ├── historian.py           # Historiador Autônomo (SESSAO/WALKTHROUGH)
│   ├── git_sync.py            # Syncer v6.0 (Learn -> Document -> Push)
│   ├── save_fix.py           # CLI para alimentação manual de memória
│   ├── .agent/custom-fixes/  # Histórico de soluções técnicas do projeto
│   └── .agent/local-kis/     # Knowledge Items locais (Regras de Negócio)
│
├── 🏗️ Project Awareness ( Hiper-Contexto )
│   └── Projetos/             # Seus projetos isolados (EC4L, iGreen, etc.)
│       └── [nome_projeto]/   # Contexto específico e código local
│
└── 📖 Documentation & Guides
    ├── ANTIGRAVITY_CORE.md   # Especificação técnica v5
    ├── ANTIGRAVITY_MAP.md    # Este mapa que você está lendo
    └── QUICKSTART.md         # Guia rápido de ativação
```

---

## 🛠️ Descrição dos Componentes Críticos

### 1. Camada de Orquestração (`agent_router.py`)
O sistema nervoso central. Ele decide quais Agentes e Skills convocar baseando-se na **Query Expansion** e refina a busca usando **Neural Reranking (TinyBERT)**.

### 2. Camada de Ação (`auto_executor.py`)
O motor da **Autonomous Bridge**. Ele usa o ChromaDB para reconhecer intenções semânticas e disparar comandos reais (vídeo, SEO, git) automaticamente.

### 2. Camada de Consciência (`monitor.py`)
A interface de transparência. É a única "janela" que permite você observar os pesos, scores neurais e decisões do sistema em tempo real.

### 3. Camada de Destilação (`knowledge_distiller.py`)
O motor de evolução. Ao final de cada tarefa concluída em `task.md`, ele analisa e "destila" a solução técnica para que ela nunca seja esquecida, gerando um **Custom Fix**.

### 4. Camada de Contexto (Hierarquia `.agent/`)
A organização em pastas categoriais (Tags) permite que o sistema saiba *onde* procurar. Se você fala de "login", o sistema foca automaticamente na pasta `security/`, economizando tokens e latência.

---

> [!TIP]
> **Dica Visual**: Imagine o Antigravity como um organismo. O `agent_router` é o cérebro, a `.agent/` é a biblioteca, o `monitor` são os olhos e o `distiller` é a memória de longo prazo. 🛸

---

## 🔗 Integrações Externas (v5.1+)

Novos layers adicionados ao ecossistema Antigravity:

### 1. Superpowers (Methodology)
**Origem:** [obra/superpowers](https://github.com/obra/superpowers) | **Stars:** 163k ⭐

Workflow completo de desenvolvimento agentic:
- `brainstorming/` - Design colaborativo
- `writing-plans/` - Planos de implementação
- `subagent-driven-development/` - Execução via subagentes
- `test-driven-development/` - RED-GREEN-REFACTOR
- `systematic-debugging/` - Debug em 4 fases

### 2. Claude SEO Extension (Marketing)
**Origem:** [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | **Stars:** 5.3k ⭐

Features avançadas de SEO:
- `/seo google report` - Relatórios PDF com gráficos
- `/seo geo` - GEO/AEO (AI Search Optimization)
- `/seo drift` - Monitoramento de mudanças
- Google APIs (PageSpeed, CrUX, GSC, GA4)

### 3. Marketing Skills Extension (Marketing)
**Origem:** [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | **Stars:** 22.8k ⭐

CRO e Copywriting:
- Page CRO, Signup CRO, Form CRO
- Copywriting (AIDA, PAS frameworks)
- Cold email, Email sequences
- A/B Testing framework

### 4. Context Engineering (AI)
**Origem:** [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | **Stars:** 15.2k ⭐

Otimização de contexto:
- Progressive disclosure pattern
- Memory architecture
- Context compression
- Lost-in-the-middle prevention

### 5. NotebookLM Integration (AI)
**Origem:** [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) | **Stars:** 6k ⭐

RAG source-grounded:
- Google NotebookLM API integration
- Source-grounded responses
- Low hallucination rate
- Minimal token cost

### 6. Remotion (Frontend)
**Origem:** [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | **Stars:** 44.2k ⭐

Video generation via React:
- `/remotion init` - Iniciar projeto Remotion
- `/remotion dev` - Development server
- `/remotion build` - Build vídeo
- Templates: intro, social, presentation, logo

### 7. Pretext (Frontend/Performance)
**Origem:** [chenglou/pretext](https://github.com/chenglou/pretext) | **Stars:** 46.3k ⭐
- Medição de texto sem DOM reflow.
- Alta performance em listas virtualizadas.

### 8. Code Review Graph (Architecture)
**Origem:** [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | **Stars:** 15.5k ⭐
- Mapa estrutural do código via Tree-sitter.
- Análise de "Blast Radius" para refatorações seguras.
- Integração nativa com MCP e Antigravity Neural Engine.

### 9. The Pentagon of Perfection (Design & Taste)
**Origem:** [Multi-repo] | **Status:** Ativo v6.5
- **Impeccable**: Compilação de intenção de design para IA.
- **Huashu-Design**: Filosofia e revisão de UI em 5 dimensões.
- **UI/UX Pro Max**: Padrões profissionais multi-plataforma.
- **Taste-Skill**: Filtro obrigatório de refinamento estético anti-slop.

### 10. Playwright (Automation)
**Origem:** [microsoft/playwright](https://github.com/microsoft/playwright) | **Status:** Infraestrutura v7.0
- Automação industrial para auditoria de UI e testes visuais.
- Base para o futuro motor de "Auto-Cura" (Auto-Healing).

---

> [!NOTE]
> **Zero conflitos** - Todos os repositórios externos foram analisados contra o `.agent/` existente. Skills de SEO já presentes foram extendidas, não substituídas. Novas categorias (methodology, context-engineering) são complementares.
