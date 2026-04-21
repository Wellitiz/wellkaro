"""
Sistema RAG de Habilidades Antigravity
Automatiza a busca e seleção de agentes e skills para seus projetos.
"""

import os
import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
ROOT_DIR = Path(__file__).parent
sys.path.insert(0, str(ROOT_DIR))

from agent_router import build_optimized_context, retrieve_documents


def get_context_for_project(prompt: str, n_agents: int = 1, n_skills: int = 2) -> str:
    """
    Retorna o contexto otimizado para um determinado prompt.

    Args:
        prompt: O que você quer fazer no seu projeto
        n_agents: Número de agentes a buscar (padrão: 1)
        n_skills: Número de skills a buscar (padrão: 2)

    Returns:
        Contexto formatado pronto para ser usado como System Prompt
    """
    return build_optimized_context(prompt, n_agents, n_skills)


def list_available_agents() -> list:
    """Lista todos os agentes disponíveis no ChromaDB."""
    result = retrieve_documents("development programming", n_agents=100, n_skills=0)
    return result["agents"]


def list_available_skills() -> list:
    """Lista todas as skills disponíveis no ChromaDB."""
    result = retrieve_documents("development programming", n_agents=0, n_skills=100)
    return result["skills"]


def search_skills(query: str, limit: int = 5) -> dict:
    """
    Busca skills específicas por tema.

    Args:
        query: Termo de busca (ex: "nextjs prisma upload")
        limit: Número máximo de resultados

    Returns:
        Dicionário com agents e skills encontrados
    """
    return retrieve_documents(query, n_agents=limit, n_skills=limit)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Sistema RAG Antigravity")
    parser.add_argument("prompt", nargs="?", help="Prompt para buscar contexto")
    parser.add_argument("--agents", "-a", type=int, default=1, help="Número de agentes")
    parser.add_argument("--skills", "-s", type=int, default=2, help="Número de skills")
    parser.add_argument(
        "--list-agents", "-la", action="store_true", help="Listar todos os agentes"
    )
    parser.add_argument(
        "--list-skills", "-ls", action="store_true", help="Listar todas as skills"
    )
    parser.add_argument("--search", type=str, help="Buscar por termo específico")

    args = parser.parse_args()

    if args.list_agents:
        print("Agentes disponíveis:")
        for agent in list_available_agents():
            print(f"  - {agent['name']} (score: {agent['score']:.2f})")
    elif args.list_skills:
        print("Skills disponíveis:")
        for skill in list_available_skills():
            print(f"  - {skill['name']} (score: {skill['score']:.2f})")
    elif args.search:
        result = search_skills(args.search)
        print(f"Busca por: {args.search}")
        print(f"\nAgentes: {[a['name'] for a in result['agents']]}")
        print(f"Skills: {[s['name'] for s in result['skills']]}")
    elif args.prompt:
        context = get_context_for_project(args.prompt, args.agents, args.skills)
        print(context)
    else:
        parser.print_help()
