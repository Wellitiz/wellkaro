# 🔱 Antigravity Context Engine: A Trindade de Identificação

O Antigravity v6.7 utiliza uma arquitetura de três camadas para garantir que cada alteração de código seja feita com precisão cirúrgica e consciência total do sistema.

---

## 🏗️ As 3 Camadas de Consciência

### 1. Camada Semântica (ChromaDB)
*   **Função**: Recuperação Vetorial.
*   **Como funciona**: Transforma o código em coordenadas matemáticas (embeddings). Ao receber uma tarefa, o Chroma localiza os arquivos que possuem o "significado" mais próximo da solicitação, ignorando barreiras de linguagem ou sintaxe.
*   **Analogy**: O Chroma é o bibliotecário que encontra todos os livros sobre um tema específico em milissegundos.

### 2. Camada Neural (TinyBERT Reranker)
*   **Função**: Filtro de Precisão Local.
*   **Como funciona**: Utiliza o modelo `TinyBERT-L-2-v2` rodando localmente. Ele analisa os resultados do Chroma e faz uma comparação profunda (Cross-Encoding) entre a sua pergunta e o conteúdo do arquivo.
*   **Impacto**: Elimina alucinações. Se o Chroma trouxer um arquivo irrelevante, o TinyBERT o descarta antes que ele chegue ao cérebro da IA.

### 3. Camada Estrutural (Knowledge Graph)
*   **Função**: Mapeamento de Dependências.
*   **Como funciona**: Constrói um grafo de conexões entre os arquivos. Ele entende Imports, chamadas de funções e variáveis globais.
*   **Impacto**: Identifica o **Blast Radius** (Raio de Impacto). Ele garante que, se você mudar algo em um lugar, o sistema saiba exatamente quais outros pontos precisam de ajuste para evitar bugs.

---

## 🔄 Como tudo funciona em 1 segundo

Quando você envia um comando, o motor entra em um ciclo hiper-veloz:

1.  **CAPTAÇÃO**: O sistema entende sua intenção.
2.  **SEARCH (Chroma)**: Busca os "candidatos" semânticos no banco de 56k documentos.
3.  **RE-RANK (TinyBERT)**: A IA local seleciona a "elite" dos arquivos (os 3 ou 5 mais precisos).
4.  **GRAPH SCAN**: O Grafo verifica as conexões desses arquivos com o restante do projeto.
5.  **INJEÇÃO**: O prompt final é montado com o código exato, as regras de design e o mapa de impacto.

---

> [!IMPORTANT]
> **Precisão Cirúrgica**: Esta arquitetura permite que o Antigravity trabalhe em projetos massivos com a mesma velocidade e segurança de um projeto pequeno. 🛸
