# 🔱 Antigravity Context Engine v7.0: A Trindade de Identificação + Performance Guard

O Antigravity v7.0 utiliza uma arquitetura de **quatro camadas** para garantir que cada alteração de código seja feita com precisão cirúrgica, consciência total do sistema e performance de elite.

---

## 🏗️ As 4 Camadas de Consciência

### 1. Camada Semântica (ChromaDB)
*   **Função**: Recuperação Vetorial.
*   **Como funciona**: Transforma o código em coordenadas matemáticas (embeddings). Ao receber uma tarefa, o Chroma localiza os arquivos que possuem o "significado" mais próximo da solicitação.
*   **Analogy**: O Chroma é o bibliotecário que encontra todos os livros sobre um tema em milissegundos.

### 2. Camada Neural (TinyBERT Reranker)
*   **Função**: Filtro de Precisão Local.
*   **Como funciona**: Utiliza o modelo `TinyBERT-L-2-v2` rodando localmente. Ele analisa os resultados do Chroma e faz uma comparação profunda (Cross-Encoding) entre a sua pergunta e o conteúdo do arquivo.
*   **Impacto**: Elimina alucinações. Se o Chroma trouxer um arquivo irrelevante, o TinyBERT o descarta.

### 3. Camada Estrutural (Graph Scan v6.7)
*   **Função**: Mapeamento de Dependências + Blast Radius.
*   **Como funciona**: Detecta imports, chamadas de funções e calcula risco de impacto.
*   **Features**: High-impact file detection, Risk scoring (low/medium/high), Skills de alto impacto alert.

### 4. Camada de Performance (PEP v3.0 Guard) ⚡ NOVO
*   **Função**: Prevenção de regressões de performance em tempo de build.
*   **Como funciona**: Após cada build de produção, o sistema valida automaticamente:
    1. **SSR Content Check**: O `out/index.html` contém `<h1>` real? Se encontrar div vazia, aborta.
    2. **LCP Visibility Check**: Nenhum elemento acima da dobra tem `opacity: 0`?
    3. **CSS Keyframes Check**: `@keyframes` estão fora do `@theme {}`?
    4. **Bundle Size Check**: Three.js/Globe não está no bundle principal?
*   **Regras Críticas Integradas**:
    - Providers (`LanguageProvider`, `ThemeProvider`) NUNCA bloqueiam renderização com `if (!mounted) return <div />`
    - Animações acima da dobra usam apenas `transform`, sem `opacity: 0`
    - `framer-motion` proibido no caminho crítico (usar CSS nativo ou `IntersectionObserver`)
    - Recursos de terceiros (CDN de bandeiras, fontes externas) são hospedados localmente
*   **Impacto**: Garante que nenhum projeto vá para produção com erros que quebram a pontuação do PageSpeed.

---

## 🔄 Como tudo funciona em 1 segundo

Quando você envia um comando, o motor entra em um ciclo hiper-veloz:

1.  **CAPTAÇÃO**: O sistema entende sua intenção.
2.  **SEARCH (Chroma)**: Busca os "candidatos" semânticos no banco de 56k documentos.
3.  **RE-RANK (TinyBERT)**: A IA local seleciona a "elite" dos arquivos.
4.  **GRAPH SCAN**: O Grafo verifica as conexões desses arquivos com o restante do projeto.
5.  **PEP GUARD**: Valida que as alterações não violam nenhuma regra de performance.
6.  **INJEÇÃO**: O prompt final é montado com o código exato, as regras de design e o mapa de impacto.

---

## 📋 Erros Reais Prevenidos pelo PEP v3.0

| Erro | Causa Real | Regra PEP |
| :--- | :--- | :--- |
| `NO_LCP` (Fatal) | `LanguageProvider` retornava div vazia no SSR | Regra Zero |
| `NO_LCP` (Desktop) | Animação CSS com `opacity: 0` no Hero | Regra 1 |
| Animações quebradas | `@keyframes` dentro de `@theme` no Tailwind v4 | Regra 4 |
| Bundle JS 650KB | Three.js no carregamento inicial | Regra 3 |
| Console warnings | `<link preload>` manual conflitando com Next.js | Regra 5 |
| Erros 404 no console | Next.js RSC `.txt` files sem rewrite no Apache | Regra 6 |
| Cache TTL 7 dias | `.htaccess` sem headers `immutable` | Regra 6 |

---

> [!IMPORTANT]
> **Precisão Cirúrgica + Performance de Elite**: Esta arquitetura de 4 camadas permite que o Antigravity trabalhe em projetos massivos com velocidade, segurança e performance industrial. Nenhum projeto sai para produção sem passar pelo PEP Guard. 🛸
