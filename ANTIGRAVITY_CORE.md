# 🛸 Antigravity Core: Ecossistema de Inteligência v5.1 (God Mode)

Bem-vindo ao **Antigravity v5.1**. Esta versão marca a transição para uma inteligência autossuficiente com integrações externas de生产力 (workflow, marketing, video).

---

## 🧠 Evolucao v5: O Salto Neural

A versao 5 introduz a camada **Neural Reranking** e o **Knowledge Distillation**, tornando o sistema capaz de eliminar ruidos e evoluir sem intervencao humana.

### 1. Motor Neural (Cross-Encoder Reranking)
O Antigravity v5 utiliza o modelo `TinyBERT-L-2-v2` localmente para refinar a precisao:
- **Fusao de Scores**: O sistema combina a busca vetorial (semantica), o Context Boosting (projeto/categoria) e a precisao do Reranker Neural.
- **Eliminacao de Alucinacoes**: O Reranker valida se o snippet recuperado realmente responde a pergunta do usuario antes de injeta-lo no prompt.

### 2. Monitor de Consciencia (Observabilidade Real-time)
Atraves do `monitor.py`, voce tem visibilidade total do "processo de pensamento" da IA:
- **Painel Persistente**: Uma interface CLI premium que exibe em tempo real:
    - Queries expandidas.
    - Agentes convocados.
    - Documentos recuperados e seus scores de precisao neural.
    - Alertas de boosts aplicados (Projeto 🎯, Solucao 🛠️, Categoria 🏷️).

### 3. Self-Learning (Knowledge Distiller)
O sistema agora aprende com o proprio sucesso:
- **`knowledge_distiller.py`**: Motor que analisa tarefas concluidas no `task.md` e extrai solucoes tecnicas para o repositorio de `custom-fixes`.
- **Aprendizado Continuo**: Cada bug corrigido gera uma memoria que sera priorizada em futuras tarefas similares.

### 4. Inteligencia Categorical & Multi-Project Aware
- **Hierarquia v5**: Agrupamento de 1.300+ itens em categorias logicas (Frontend, Security, AI, etc).
- **Multi-Tagging**: Suporte a tags combinadas para contexto hibrido.

---

## 🌐 Integrações Externas v5.1

### Superpowers (Workflow Methodology)
- **Origem:** [obra/superpowers](https://github.com/obra/superpowers) (163k ⭐)
- **Arquivo:** `.agent/methodology/superpowers/`
- **Skills:** brainstorming, writing-plans, subagent-driven-dev, test-driven-dev, systematic-debugging

### Claude SEO Extension (Marketing)
- **Origem:** [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) (5.3k ⭐)
- **Arquivo:** `.agent/marketing/seo/claude-seo-extension/`
- **Features:** Google APIs, GEO/AEO, drift monitoring

### Marketing Skills Extension (CRO/Email)
- **Origem:** [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (22.8k ⭐)
- **Arquivo:** `.agent/marketing/marketing-skills-extension/`
- **Skills:** Page CRO, Signup CRO, Copywriting, Email sequences

### Context Engineering (AI)
- **Origem:** [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) (15.2k ⭐)
- **Arquivo:** `.agent/ai/context-engineering/`
- **Features:** Progressive disclosure, memory architecture

### NotebookLM Integration (AI)
- **Origem:** [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) (6k ⭐)
- **Arquivo:** `.agent/ai/notebooklm-integration/`
- **Features:** RAG source-grounded, low hallucination

### Remotion (Frontend)
- **Origem:** [remotion-dev/remotion](https://github.com/remotion-dev/remotion) (44.2k ⭐)
- **Arquivo:** `.agent/frontend/remotion/`
- **Features:** Video generation via React

---

## 🏗️ Fluxo de Trabalho Automatizado (Zero Friction)

*   **Sincronizacao Inteligente**: O Core se auto-indexa ao detectar mudancas fisicas ou estruturais.
*   **Neural Loop**: 
    1.  **Busca**: Recupera candidatos via Vetor + Keywords.
    2.  **Boost**: Aplica pesos de Projeto e Categoria.
    3.  **Rerank**: O Reranker Neural seleciona a elite dos snippets.
    4.  **Injecao**: Prompt unificado de alta fidelidade e gerado.

---

## 📂 Estrutura de Arquivos v5.1

| Arquivo/Pasta | Funcao |
| :--- | :--- |
| `index_skills.py` | Motor de indexacao e mapeamento hibrido. |
| `agent_router.py` | Orquestrador v5 com **Neural Reranking**. |
| `monitor.py` | Painel de controle e observabilidade real-time. |
| `knowledge_distiller.py` | Motor de aprendizado autônomo. |
| `save_fix.py` | Utilitario para alimentacao manual de memoria. |
| `chroma_db/` | Banco vetorial persistente (13.800+ documentos). |
| `.agent/methodology/superpowers/` | Superpowers workflow system |
| `.agent/frontend/remotion/` | Video generation framework |

---

## 🚀 DevOps & IA Engineering

O Antigravity v5 e uma ferramenta de engenharia de IA preparada para escala:
- **Model Isolation**: Modelos neurais rodam localmente para privacidade total.
- **Cross-Project Intelligence**: Memoria compartilhada entre todos os seus projetos sob gestao.

---

> [!TIP]
> Para ativar o Painel de Consciencia, abra um novo terminal e rode: `python monitor.py`. 🛸
