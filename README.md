# 🛸 Antigravity-Welltiz: Neural Consciousness Ecosystem v6.2

[![Antigravity v6.2](https://img.shields.io/badge/Engine-v6.2%20Consciousness-magenta?style=for-the-badge)](https://github.com/Wellitiz/Antigravity-Welltiz)
[![Database](https://img.shields.io/badge/Vector%20DB-ChromaDB-blue?style=for-the-badge)](https://www.trychroma.com/)
[![Model](https://img.shields.io/badge/Neural%20Reranker-TinyBERT-orange?style=for-the-badge)](https://huggingface.co/cross-encoder/ms-marco-TinyBERT-L-2-v2)
[![Design](https://img.shields.io/badge/Design-Stitch--MD-green?style=for-the-badge)](https://github.com/VoltAgent/awesome-design-md)

**Antigravity-Welltiz** é um ecossistema de inteligência autônoma de ultra-fidelidade, projetado para transcender a automação convencional através de recuperação semântica profunda, reranking neural e ciclos de aprendizado contínuo.

---

## 🧠 The Neural Engine (Engenharia de Elite)

O coração do Antigravity não é apenas um script, mas um pipeline de processamento de linguagem natural (NLP) multi-camadas:

### 1. Camada de Vetorização (ChromaDB)
Utilizamos o **ChromaDB** como nossa memória de longo prazo. Cada uma das 1.300+ habilidades e fragmentos de código é processado e armazenado como um embedding vetorial em um espaço n-dimensional.
- **RAG (Retrieval-Augmented Generation)**: Quando você faz um prompt, o sistema realiza uma busca de vizinhos mais próximos (KNN) para recuperar o contexto mais relevante instantaneamente.

### 2. Reranking Neural (TinyBERT Cross-Encoder)
A busca vetorial por si só pode ser imprecisa. Para garantir fidelidade de 100%, implementamos o modelo **Cross-Encoder TinyBERT-L-2-v2**:
- **Pente Fino**: O sistema recupera os top 10 candidatos do ChromaDB e os submete ao TinyBERT.
- **Scoring Neural**: O modelo analisa a relação semântica exata entre sua pergunta e o conteúdo recuperado, reordenando-os por relevância lógica real, eliminando alucinações.

### 3. Context Boosting Protocol
Aplicamos pesos dinâmicos baseados no estado do sistema:
- **🎯 Project Boost (1.5x)**: Prioriza arquivos do repositório em que você está trabalhando.
- **🛠️ Solution Boost (1.3x)**: Prioriza correções técnicas e lições aprendidas anteriormente.
- **🏷️ Category Boost (1.2x)**: Prioriza domínios de conhecimento específicos detectados no prompt.

---

## 🔄 The Consciousness Loop (v6.1 Workflow)

O Antigravity-Welltiz opera em um ciclo fechado de inteligência:

1.  **Observação**: O `monitor.py` visualiza cada etapa do pensamento da IA.
2.  **Debate (Multi-Agent Debate)**: Três especialistas (**CyberGuard**, **NitroStream**, **NexusPrime**) debatem a melhor implementação técnica.
3.  **Execução**: O `run.py` (Ponte Autônoma) decide o comando ideal ou plano a seguir.
4.  **Aprendizado (Knowledge Distiller)**: Ao final da tarefa, o sistema extrai o conhecimento fixo e o destila em arquivos de memória.
5.  **Design Intelligence**: O sistema agora exige e adere ao protocolo `DESIGN.md` para garantir UI/UX premium constante.
6.  **Documentação (Historian)**: O sistema redige automaticamente o progresso em `SESSAO.md`.
7.  **Persistência (Git Sync)**: Tudo é versionado e sincronizado via `git_sync.py`.

---

## 📂 Project Architecture

```text
ANTIGRAVITY_WELLTIZ/
├── 🧠 Intelligence Core
│   ├── agent_router.py       # Orquestrador Neural (TinyBERT + ChromaDB Link)
│   ├── auto_executor.py      # Motor de Intenção e Gatilhos Semânticos
│   ├── run.py                 # Ponto de Entrada Universal (The Bridge)
│   └── index_skills.py        # Pipeline de Embedding e Indexação Vetorial
├── 🔄 Learning & Persistence
│   ├── historian.py           # Gerador de Documentação Autônoma
│   ├── knowledge_distiller.py  # Extração de Lições Aprendidas
│   └── git_sync.py             # Sincronização Consciente v6.1
├── 📂 Neural Library (Cognição)
│   ├── .agent/                # Repositório de Agentes e Skills (1.300+ itens)
│   └── chroma_db/             # Database Vetorial Persistente
└── 📜 Documentation Elite
    ├── README.md              # Documentação Técnica Mestre
    ├── ANTIGRAVITY_CORE.md    # Especificação do Ecossistema
    └── QUICKSTART.md          # Guia de Ativação Rápida
```

---

## ⚡ Setup de Alta Performance

```bash
# 1. Clone & Entra
git clone https://github.com/Wellitiz/Antigravity-Welltiz.git
cd Antigravity-Welltiz

# 2. Dependências Neurais
pip install chromadb sentence-transformers rich

# 3. Ativação
python monitor.py  # Em um terminal dedicado
python run.py "sua tarefa de engenharia"
```

---

> 🛸 **Antigravity-Welltiz** - *Where Neural Intelligence Meets Autonomous Execution.*
