# 🛸 Antigravity Core: Ecossistema de Inteligência v5 (God Mode)

Bem-vindo ao **Antigravity v5**. Esta versao marca a transicao para uma inteligencia autossuficiente, onde o sistema nao apenas recupera dados, mas refina seu proprio pensamento e aprende com cada tarefa concluida.

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

## 🏗️ Fluxo de Trabalho Automatizado (Zero Friction)

*   **Sincronizacao Inteligente**: O Core se auto-indexa ao detectar mudancas fisicas ou estruturais.
*   **Neural Loop**: 
    1.  **Busca**: Recupera candidatos via Vetor + Keywords.
    2.  **Boost**: Aplica pesos de Projeto e Categoria.
    3.  **Rerank**: O Reranker Neural seleciona a elite dos snippets.
    4.  **Injecao**: Prompt unificado de alta fidelidade e gerado.

---

## 📂 Estrutura de Arquivos v5

| Arquivo/Pasta | Funcao |
| :--- | :--- |
| `index_skills.py` | Motor de indexacao e mapeamento hibrido. |
| `agent_router.py` | Orquestrador v5 com **Neural Reranking**. |
| `monitor.py` | Painel de controle e observabilidade real-time. |
| `knowledge_distiller.py` | Motor de aprendizado autônomo. |
| `save_fix.py` | Utilitario para alimentacao manual de memoria. |
| `chroma_db/` | Banco vetorial persistente (14.000+ documentos). |

---

## 🚀 DevOps & IA Engineering

O Antigravity v5 e uma ferramenta de engenharia de IA preparada para escala:
- **Model Isolation**: Modelos neurais rodam localmente para privacidade total.
- **Cross-Project Intelligence**: Memoria compartilhada entre todos os seus projetos sob gestao.

---

> [!TIP]
> Para ativar o Painel de Consciencia, abra um novo terminal e rode: `python monitor.py`. 🛸
