# Sistema RAG - Habilidades Antigravity

## Estrutura Criada

```
Antigravity (Raiz)
├── .agent/                    # 1.380+ habilidades indexadas
├── chroma_db/                 # Banco vetorial (busca semântica)
├── index_skills.py            # Script de indexação
├── agent_router.py            # Motor de busca
├── rag_system.py              # CLI principal
├── rag_config.example         # Modelo de config para projetos
├── setup_project.py           # Setup por projeto
├── RAG_README.md              # Documentação
├── requirements.txt          # chromadb
└── .gitignore                # Ignora chroma_db/

Projetos/
├── zip_check/                 # Seu projeto
├── Veiculos/                  # Seu projeto
└── ...                       # Outros projetos
```

## Comandos

```bash
# Buscar contexto otimizado
python rag_system.py "Criar API de upload"

# Listar agentes
python rag_system.py --list-agents

# Listar skills
python rag_system.py --list-skills

# Buscar por tema
python rag_system.py --search "prisma mysql"

# Reindexar (se adicionar novas habilidades)
python index_skills.py

# Configurar um projeto específico
cd Projetos/zip_check
python ../setup_project.py
```

## Integração com OpenCode/Antigravity

Antes de pedir algo ao agente, use:

```
@rag "sua tarefa aqui"
```

Ou importe no código:

```python
from rag_system import get_context_for_project

context = get_context_for_project("Criar rota de upload de veículos")
# Use context como system prompt
```

## Funcionamento

1. **Indexação**: `index_skills.py` varre `.agent/` e indexa 2.354 documentos
2. **Classificação**: Cada documento é classificado como `agent` ou `skill`
3. **Busca**: `agent_router.py` faz busca vetorial separada para agentes e skills
4. **Resultado**: Context otimizado com os agentes/skills mais relevantes

---

**Mantido em:** `C:\Users\welli\Downloads\Antigravity`