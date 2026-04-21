#!/usr/bin/env python3
"""
Setup do Sistema RAG para projetos Antigravity
Execute este script em cada projeto para configurar a integração com o RAG.
"""

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
RAG_PATH = PROJECT_ROOT / "chroma_db"
PROJECT_NAME = Path.cwd().name


def setup_project():
    """Configura o projeto atual para usar o sistema RAG."""

    print(f"Configurando RAG para projeto: {PROJECT_NAME}")
    print(f"Localização do ChromaDB: {RAG_PATH}")

    # Criar link simbólico ou copiar referência
    if not RAG_PATH.exists():
        print("ERRO: chroma_db não encontrado. Execute index_skills.py primeiro.")
        return False

    # Verificar se existe .env ou criar configuração
    rag_config = Path(".rag_config")
    if not rag_config.exists():
        config_content = f"""# Configuração RAG para {PROJECT_NAME}
[project]
name = "{PROJECT_NAME}"
tech_stack = ""

[rag]
chroma_path = "../chroma_db"
enabled = true
"""
        rag_config.write_text(config_content)
        print(f"  ✓ Criado .rag_config")

    # Criar script de utilities se não existir
    utils_path = Path("rag_utils.py")
    if not utils_path.exists():
        utils_content = f'''"""Utilities RAG para {PROJECT_NAME}"""
import sys
from pathlib import Path

# Adiciona o diretório raiz do Antigravity ao path
ANTIGRAVITY_ROOT = Path("{PROJECT_ROOT.as_posix()}")
sys.path.insert(0, str(ANTIGRAVITY_ROOT))

from agent_router import build_optimized_context

def get_rag_context(prompt: str) -> str:
    """Retorna contexto otimizado para seu projeto."""
    return build_optimized_context(prompt, n_agents=1, n_skills=2)
'''
        utils_path.write_text(utils_content)
        print(f"  ✓ Criado rag_utils.py")

    print(f"\n✅ Projeto {PROJECT_NAME} configurado!")
    print("\nUso:")
    print('  python rag_utils.py "sua tarefa"')
    print("  # ou no código:")
    print("  from rag_utils import get_rag_context")
    print('  context = get_rag_context("minha tarefa")')


if __name__ == "__main__":
    setup_project()
