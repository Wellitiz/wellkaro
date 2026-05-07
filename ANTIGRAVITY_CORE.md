# 🛸 Antigravity Core: Ecossistema de Inteligência v7.0 (Battle-Hardened Edition)

Bem-vindo ao **Antigravity v7.0**. Esta versão consolida as lições da batalha de performance do projeto Verdeon, transformando cada bug em lei permanente.

---

## 🧠 Evolução v7.0: Performance Battle-Hardened

A versão 7.0 representa a maturidade total do sistema: memória plena + performance industrial.

### 1. Total Recall (56.907 Documentos Indexados)
- **Indexação 100% Concluída**: Mais de 56 mil documentos de inteligência ativos no ChromaDB.
- **Filtro Inteligente**: Ignora ruídos (`node_modules`, `vendor`, `bin`) focando na lógica de alto nível.
- **Recuperação de Contexto Zero-Prompt**: Recuperação automática de skills dos 88 repositórios.

### 2. ⚡ PEP v3.0 (Performance Excellence Protocol — Battle-Tested)
A performance 90+ agora é lei nativa. O PEP v3.0 foi forjado na batalha real do projeto Verdeon:

#### Regras Críticas (Aprendidas na Dor):
| Regra | Problema que Previne | Severidade |
| :--- | :--- | :--- |
| **Nunca bloquear SSR com `if (!mounted) return <div/>`** | HTML vazio → NO_LCP fatal | 🔴 CRÍTICA |
| **Animações sem `opacity: 0` acima da dobra** | Conteúdo invisível → NO_LCP | 🔴 CRÍTICA |
| **`@keyframes` fora do `@theme {}`** | Animações não funcionam no Tailwind v4 | 🟡 ALTA |
| **ScrollReveal com CSS nativo, não framer-motion** | Bundle JS inflado (+200KB) | 🟡 ALTA |
| **Globe/3D com IntersectionObserver** | Three.js no bundle inicial (+650KB) | 🟡 ALTA |
| **Bandeiras/ícones locais, sem CDN** | Dependência de terceiros | 🟢 MÉDIA |
| **Cache 1 ano para `_next/static/`** | Cache TTL insuficiente | 🟢 MÉDIA |

#### Checklist de Build Obrigatório:
Antes de **todo** deploy, verificar:
1. `out/index.html` contém `<h1>` real (não div vazia)
2. Nenhum `opacity: 0` acima da dobra
3. `@keyframes` fora do `@theme`
4. `.htaccess` com RSC fix e cache 1 ano

### 3. Autonomia Estética (Design Consciousness)
- **DESIGN.md Protocol**: O sistema é 100% guiado pela identidade visual via tokens na raiz.

### 4. Motor Neural (Neural Reranking v6.7)
- **TinyBERT-L-2-v2**: Cross-Encoder local para eliminação de alucinações.
- **Context Validation**: Valida se o snippet é a melhor solução antes de injetá-lo no prompt.

### 5. Camada Estrutural (Graph Scan v6.7)
- **Dependency Scan**: Detecta imports (TS/JS/Python/Prisma).
- **Risk Scoring**: Classifica arquivos como low/medium/high.
- **Impact Score**: Métrica numérica do risco total.

---

## 📂 Estrutura de Arquivos v7.0

| Arquivo/Pasta | Função |
| :--- | :--- |
| `index_skills.py` | Motor de indexação ultra-veloz. |
| `chroma_db/` | Banco vetorial de 1.98 GB com 56.907 documentos. |
| `.agent/specialists/bulk_import/` | 88 repositórios especializados. |
| `ANTIGRAVITY_CORE.md` | Especificação técnica v7.0. |
| `PEP v3.0` | Performance Excellence Protocol (Knowledge Item). |

---

## 🚀 DevOps & IA Engineering

O Antigravity v7.0 opera como um Arquiteto Sênior Autônomo com consciência de performance integrada. Cada projeto novo nasce com as regras do PEP v3.0 já aplicadas.

---

> [!TIP]
> **Battle-Hardened**: Cada regra do PEP v3.0 foi aprendida com um bug real. Se o conhecimento existe na biblioteca, o Antigravity v7.0 irá encontrá-lo, aplicá-lo e validá-lo automaticamente. 🛸
