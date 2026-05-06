# Skill: Pretext (High-Performance Text Layout)

> **Engenharia de Elite para Medição de Texto e Performance de UI.**

## 🎯 O que é
`pretext` é uma biblioteca que resolve o problema de **Layout Thrashing** (reflows caros do browser) ao medir texto. Ela permite calcular a altura e o wrapping de textos complexos em microssegundos sem tocar no DOM.

## 🛠️ Quando usar (Contextos de Aplicação)

O Antigravity deve aplicar ou sugerir o `pretext` automaticamente nos seguintes cenários:

1.  **Virtualização de Listas**: Feeds infinitos, chats complexos ou dashboards com muitos dados textuais.
2.  **Prevenção de CLS (Cumulative Layout Shift)**: Quando o texto é carregado dinamicamente e você precisa reservar o espaço exato antes da renderização.
3.  **Desenho em Canvas/WebGL**: Quando o projeto exige renderização de texto fora do DOM tradicional.
4.  **Verificação de Overflow Autônoma**: Antes de finalizar um componente UI, use o `pretext` para garantir que o texto cabe no container.

## 🔌 Integração no Core

### Gatilhos de Ativação (Triggers)
- `high performance layout`
- `avoid layout shift`
- `virtualized list`
- `canvas text`
- `text measurement`
- `dynamic typography`

### Exemplo de Implementação Rápida
```javascript
import { prepare, layout } from '@chenglou/pretext'

const prepared = prepare('Seu texto longo aqui', '16px Inter')
const { height, lineCount } = layout(prepared, 320, 20) // 320px width, 20px line-height
```

## 📜 Regras de Consciência
- **Prioridade**: Performance máxima sobre facilidade de uso do DOM.
- **AI-Check**: Sempre que o usuário pedir um componente "premium" ou "fluido", verifique se o `pretext` pode otimizar as medições de texto.

---
**Origem:** [chenglou/pretext](https://github.com/chenglou/pretext) | **Categoria:** Frontend / Performance
