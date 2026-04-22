# 🛸 Antigravity Core: Ecossistema de Inteligência v6.1 (Antigravity-Welltiz)

Bem-vindo ao **Antigravity v6.1**. Esta versão refina as ferramentas de consciência introduzidas na v6.0, adicionando curadoria técnica para novas habilidades e consulta histórica sob demanda.

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
O sistema agora aprende com o próprio sucesso:
- **Integração Git**: O ciclo de aprendizado agora roda automaticamente antes de cada `git push`, garantindo que o conhecimento destilado viaje pelos seus dispositivos.

### 4. Ponte de Curadoria (Curatorship Bridge v6.1)
A expansão de conhecimento agora é inteligente e deliberada:
- **Detecção Automática**: Links do GitHub enviados no prompt são imediatamente interceptados para análise.
- **Relatório de Viabilidade**: O sistema gera uma análise de **Vantagens e Desvantagens** do repositório antes de oferecer a indexação definitiva.

### 5. Consulta Histórica Inteligente (v6.1)
Acesse seu progresso instantaneamente através de linguagem natural:
- **"Analise a sessão anterior"**: Novo comando unificado que extrai o relatório mais recente do Historiador e fornece um resumo executivo para retomada rápida de contexto.

---

## 🚀 Pilares Antigravity v6.0 (Legacy)

### 1. Universal Skill Auto-Generator (Expansão Infinita)
O Antigravity agora pode aprender qualquer tecnologia do planeta:
- **`skill_generator.py`**: Permite importar qualquer repositório GitHub diretamente para a biblioteca `.agent/`.
- **Análise Autônoma**: O sistema clona, analisa e gera a documentação de suporte (`SKILL.md`) sozinho.

### 2. Autonomous Session Historian (Auto-Documentação)
Diga adeus ao trabalho manual de documentação:
- **`historian.py`**: Analisa cada mudança de código e tarefa concluída para redigir o `SESSAO.md` e o `walkthrough.md`.
- **Memória Histórica**: Integrado ao Sync, garantindo que cada push contenha um registro impecável do progresso.

### 3. Multi-Agent Team Debate (Refino Extremo)
A inteligência do orquestrador foi elevada ao nível de diretoria:
- **Mesa Redonda Virtual**: Cada prompt é analisado simultaneamente por um **Auditor de Segurança**, um **Engenheiro de Performance** e um **Arquiteto de Sistemas**.
- **Consenso Antigravity**: O output final é o resultado de um debate técnico, eliminando refação e erros básicos.

---

## 🌐 Integrações Externas v5.1

### Superpowers (Workflow Methodology)
- **Origem:** [Wellitiz/Antigravity-Welltiz](https://github.com/Wellitiz/Antigravity-Welltiz)
- **Arquivo:** `.agent/methodology/superpowers/`
- **Skills:** brainstorming, writing-plans, subagent-driven-dev, test-driven-dev, systematic-debugging

### Claude SEO Extension (Marketing)
- **Origem:** [Wellitiz/Antigravity-Welltiz](https://github.com/Wellitiz/Antigravity-Welltiz)
- **Arquivo:** `.agent/marketing/seo/claude-seo-extension/`
- **Features:** Google APIs, GEO/AEO, drift monitoring

### Marketing Skills Extension (CRO/Email)
- **Origem:** [Wellitiz/Antigravity-Welltiz](https://github.com/Wellitiz/Antigravity-Welltiz)
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
