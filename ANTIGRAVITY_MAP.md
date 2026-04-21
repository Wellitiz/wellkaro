# 🛸 Antigravity v5 God Mode: Mapa do Ecossistema

Este documento fornece a visualização estrutural completa do ecossistema Antigravity, detalhando a função de cada camada e arquivo no sistema.

---

## 🗺️ Mapa Arquitetural (Project Tree)

```text
ANTIGRAVITY_ROOT/
├── 🧠 Intelligence & RAG Core ( O Coração )
│   ├── agent_router.py       # Orquestrador v5 (Neural Reranking + Boosting)
│   ├── index_skills.py       # Motor de Indexação Híbrida e Multi-Tagging
│   ├── auto_rag.py           # Planejador Automático e Ativador de Briefings
│   └── monitor.py             # Painel de Consciência (Monitor Real-time)
│
├── 📂 Knowledge Base ( Memória Global )
│   ├── .agent/               # Repositório de 1.300+ Agentes e Skills
│   │   ├── ai/               # Modelos, Prompts e Especialistas em LLM
│   │   ├── frontend/         # React, Next.js, UI/UX, CSS, Tailwind
│   │   ├── backend/          # Node, Python, Databases, APIs
│   │   ├── security/         # Auditoria, Auth, Proteção, Pentest
│   │   └── ... (mais 50+ categorias multitag)
│   └── chroma_db/            # Banco Vetorial (HNSW Index v5)
│
├── 🔄 Learning Loop ( Feedback de Longo Prazo )
│   ├── knowledge_distiller.py # Destilador Autônomo de fix/ki
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
O sistema nervoso central. Ele decide quaisAgentes e Skills convocar baseando-se na **Query Expansion** (nuances semânticas) e refina a busca usando **Neural Reranking**.

### 2. Camada de Consciência (`monitor.py`)
A interface de transparência. É a única "janela" que permite você observar os pesos, scores neurais e decisões do sistema em tempo real.

### 3. Camada de Destilação (`knowledge_distiller.py`)
O motor de evolução. Ao final de cada tarefa concluída em `task.md`, ele analisa e "destila" a solução técnica para que ela nunca seja esquecida, gerando um **Custom Fix**.

### 4. Camada de Contexto (Hierarquia `.agent/`)
A organização em pastas categoriais (Tags) permite que o sistema saiba *onde* procurar. Se você fala de "login", o sistema foca automaticamente na pasta `security/`, economizando tokens e latência.

---

> [!TIP]
> **Dica Visual**: Imagine o Antigravity como um organismo. O `agent_router` é o cérebro, a `.agent/` é a biblioteca, o `monitor` são os olhos e o `distiller` é a memória de longo prazo. 🛸
