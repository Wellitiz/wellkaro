# Remotion - Video Generation Framework

> **Crie vídeos programaticamente usando React**

[Remotion](https://github.com/remotion-dev/remotion) é um framework para criar vídeos usando React, CSS, Canvas, SVG, WebGL e todo o poder da programação.

## 🎯 O que é

O Remotion permite criar vídeos usando código JavaScript/TypeScript:

```tsx
const Video = () => {
  return (
    <div>
      <h1>Olá Mundo!</h1>
    </div>
  );
};
```

## 🎬 Quando Usar

- **Content marketing** - Vídeos explicativos, tutorials
- **Social media** - Shorts, Reels, TikTok
- **Product demos** - Demonstrações de produto
- **Data viz** - Gráficos animados
- **Meet recaps** - Resumos de reuniões

## 🛠️ Setup

### Instalação

```bash
npm install remotion
# ou
npx create-video@latest
```

### Comandos

```bash
remotion dev          # Development server
remotion build       # Build para produção
remotion studio     # UI online
remotion lambda    # Deploy AWS Lambda
```

## 📋 Comandos Antigravity

Use estes comandos no seu projeto:

```
/remotion init         # Iniciar projeto Remotion
/remotion dev         # Iniciar development server
/remotion build      # Build vídeo
/remotion template   # Listar templates disponíveis
/remotion studio    # Abrir Studio (requ setup)
```

## 🎨 Exemplo Básico

```tsx
import { Composition } from 'remotion';

export const MyVideo = () => {
  return (
    <div style={{
      backgroundColor: '#000',
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center'
    }}>
      <h1 style={{ color: 'white', fontSize: 80 }}>
        Hello World!
      </h1>
    </div>
  );
};
```

## 📊 Recursos

- **HTML/CSS** - Tudo do CSS disponível
- **Canvas** - Renderização 2D/3D
- **SVG** - Gráficos vetoriais
- **WebGL** - OpenGL via Three.js

## 🔗 Templates Incluídos

| Template | Descrição |
|----------|-----------|
| `intro` | Introdução com logo e animação |
| `social` | Template para social media |
| `presentation` | Slides animados |
| `logo` | Animações de logo |

## 📁 Estrutura do Projeto

```
project/
├── src/
│   ├── Root.tsx
│   ├── Video.tsx
│   └── components/
│       ├── Title.tsx
│       ├── Subtitle.tsx
│       └── OutroComponente.tsx
├── package.json
└── remotion.config.ts
```

## 🔐 Licença

⚠️ **Importante:** Remotion tem licence especial. Leia em:
[remotion.dev/license](https://remotion.dev/license)

Uso pessoal = Grátis
Comercial = Pode requerer licença

---

**Origem:** [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | **Stars:** 44.2k ⭐