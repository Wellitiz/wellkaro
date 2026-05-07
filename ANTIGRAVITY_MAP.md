# 🛸 Antigravity v7.0 Battle-Hardened: Mapa do Ecossistema

Este documento fornece a visualização estrutural completa e atualizada do ecossistema Antigravity v7.0.

---

## 🗺️ Mapa Arquitetural (Project Tree)

```text
ANTIGRAVITY_ROOT/
├── 🧠 Intelligence & RAG Core ( O Coração )
│   ├── agent_router.py       # Orquestrador v7.0 (TinyBERT + Graph Scan + PEP Guard)
│   ├── index_skills.py       # Motor v5 (Real-time Scanning Feedback)
│   ├── run.py                 # Ponto de Entrada Universal
│   ├── monitor.py             # Monitor de Consciência Real-time
│   ├── auto_rag.py            # Planejador de contexto automático
│   ├── auto_executor.py       # Executor de comandos autônomos
│   ├── historian.py           # Historiador de sessão
│   └── knowledge_distiller.py # Destilador de conhecimento
│
├── 📂 Knowledge Base ( Memória Global )
│   ├── .agent/               # Repositório de 1.500+ Agentes e Skills [v7.0]
│   │   ├── specialists/      # Specialized Knowledge Clusters
│   │   │   └── bulk_import/  # 88 repositories / 56k docs indexed [v7.0]
│   │   └── design/           # Design System Protocol (DESIGN.md)
│   └── chroma_db/            # Banco Vetorial (HNSW Index v6 - 1.98GB)
│
├── ⚡ Performance Guard ( PEP v3.0 — Battle-Tested )
│   ├── PEP Protocol          # Knowledge Item com todas as regras de performance
│   └── Build Checklist       # Validação automática pós-build
│
├── 🔄 Learning Loop ( Consciência )
│   ├── git_sync.py            # Syncer v7.0
│   └── .agent/local-kis/     # Knowledge Items destilados
│
├── 🏗️ Project Awareness ( Hiper-Contexto )
│   └── Projetos/             # Projetos (EC4L CRM, NossaNet, Verdeon, etc.)
│
└── 📖 Documentation & Guides
    ├── ANTIGRAVITY_CORE.md   # Especificação técnica v7.0
    ├── ANTIGRAVITY_MAP.md    # Este mapa (v7.0)
    ├── ENGINE_CONTEXT.md     # Quadra de Contexto (Chroma + TinyBERT + Graph + PEP)
    └── README.md             # Cartão de Visitas v7.0
```

---

## 🛠️ Status da Consciência v7.0

### 1. Quadra de Contexto (Completa — 4 Camadas)
O sistema opera em 4 camadas para precisão cirúrgica + performance industrial:
- **Camada 1 (Semântica)**: ChromaDB — 56.907 documentos indexados
- **Camada 2 (Neural)**: TinyBERT-L-2-v2 — Reranking e eliminação de alucinações
- **Camada 3 (Estrutural)**: Graph Scan v6.8 — Blast Radius + Risk Analysis
- **Camada 4 (Performance)**: ⚡ PEP v3.0 Guard — Validação de performance pós-build

### 2. Protocolo de Performance (Elite Benchmark — Battle-Tested)
O **PEP v3.0** foi forjado na batalha real do projeto **Verdeon Energies**, que atingiu **97/94 (Desktop/Mobile)** no PageSpeed. As regras cobrem:

| Categoria | Regras Críticas |
| :--- | :--- |
| **SSR (Regra Zero)** | Providers nunca bloqueiam renderização com div vazia |
| **Animações** | Apenas `transform` acima da dobra, sem `opacity: 0` |
| **CSS** | `@keyframes` fora do `@theme`, containment em sections |
| **JavaScript** | Globe/3D com IntersectionObserver, ScrollReveal com CSS nativo |
| **Assets** | WebP q60-70, logos 100px, cards 640px, recursos locais |
| **Deploy** | Cache 1 ano, RSC fix no .htaccess, LiteSpeed flush |

### 3. Autonomia de Skills
Com a indexação completa, o Antigravity possui "memória fotográfica" de todos os 88 repositórios de skills.

### 4. Graph Scan Integrada
Detecção de dependências em TypeScript, JavaScript, Python e Prisma com classificação de risco e alertas de impacto.

---

## 📚 Lista Mestra de Skills Integradas (88 Repositórios) [v7.0]

| Categoria | Repositórios Principais (Clusters) |
| :--- | :--- |
| **IA & Prompts** | `anthropics_skills`, `ykdojo_claude-code-tips`, `SeifBenayed_claude-code-sdk`, `agentbay-ai_agentbay-skills`, `deapi-ai_claude-code-skills`, `Square-Zero-Labs_video-prompting-skill`, `Xquik-dev_x-twitter-scraper` |
| **Desenvolvimento** | `jeffallan_claude-skills`, `Valian_linear-cli-skill`, `krodak_clickup-cli`, `testdino-hq_playwright-skill`, `obra_superpowers`, `ivan-magda_claude-code-plugin-template`, `bluzername_claude-code-terminal-title` |
| **Design & UI** | `Ashutos1997_claude-design-auditor-skill`, `oil-oil_oiloil-ui-ux-guide`, `framix-team_skill-email-html-mjml`, `glitternetwork_skills`, `takechanman1228_claude-ecom` |
| **Marketing & SEO** | `guia-matthieu_clawfu-skills`, `jonathimer_devmarketing-skills`, `conorbronsdon_avoid-ai-writing`, `product-on-purpose_pm-skills`, `TomGranot_hubspot-admin-skills`, `ykdojo_gh-star-history` |
| **Pesquisa & Dados** | `pjt222_agent-almanac`, `K-Dense-AI_claude-scientific-skills`, `HeshamFS_materials-simulation-skills`, `ykdojo_paper-search`, `shmlkv_dna-claude-analysis`, `zagmoai_public-google-drive` |
| **Especialistas** | `Digidai_product-manager-skills`, `EmblemCompany_Agent-skills`, `RioTheGreat-ai_agentfund-mcp`, `bitwize-music-studio_claude-ai-music-skills`, `omkamal_pypict-claude-skill`, `BehiSecc_VibeSec-Skill` |

> [!NOTE]
> **Status de Integração**: 100% dos arquivos foram vetorizados no `chroma_db/`. A inteligência destes especialistas é agora parte nativa da consciência neural do Antigravity v7.0. 🛸
