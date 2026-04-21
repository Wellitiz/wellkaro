#!/usr/bin/env python3
"""
Auto-RAG: Ativador Automático de Contexto
Executa automaticamente quando o usuário fornece um briefing.
"""

import sys
from pathlib import Path

# Setup path
ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

from agent_router import build_optimized_context, retrieve_documents
import json


def auto_plan_and_execute(briefing: str) -> dict:
    """
    Analisa o briefing e retorna plano completo de execução com time de especialistas.
    """
    print(f"[*] Analisando briefing: {briefing[:100]}...")

    # 1. Expandir busca para garantir cobertura total (Estratégia Antigravity)
    # Adicionamos termos técnicos comuns para puxar os melhores agentes de arquitetura e segurança
    expanded_query = f"{briefing} architecture security performance best practices expert"
    
    # Determinamos o tamanho da equipe com base na complexidade (heurística simples)
    n_agents = 5 if len(briefing) > 100 else 3
    n_skills = 7 if len(briefing) > 100 else 4

    context = build_optimized_context(expanded_query, n_agents=n_agents, n_skills=n_skills)

    # 2. Detectar tipo de projeto
    project_type = detect_project_type(briefing)
    tech_stack = detect_tech_stack(briefing)

    # 3. Gerar plano de execucao
    plan = generate_plan(briefing, project_type, tech_stack)

    return {
        "briefing": briefing,
        "project_type": project_type,
        "tech_stack": tech_stack,
        "context": context,
        "plan": plan,
    }


def detect_tech_stack(briefing: str) -> list:
    """Detecta tecnologias mencionadas no briefing com mapeamento premium."""
    briefing_lower = briefing.lower()

    techs = {
        "Next.js 15 (App Router)": ["nextjs", "next.js", "react", "next"],
        "Prisma ORM": ["prisma", "orm"],
        "PostgreSQL (Neon)": ["postgres", "postgresql", "db", "banco"],
        "Tailwind CSS v4": ["tailwind", "css", "estilo", "styling"],
        "Stripe Payments": ["stripe", "pagamento", "pagar", "checkout"],
        "Clerk Auth": ["auth", "login", "autentic", "clerk"],
        "TypeScript": ["typescript", "ts", "type script"],
    }

    detected = []
    for tech, keywords in techs.items():
        if any(k in briefing_lower for k in keywords):
            detected.append(tech)
    return detected if detected else ["Next.js", "TypeScript", "Tailwind CSS"]


def detect_project_type(briefing: str) -> str:
    """Detecta o tipo de projeto com categorização Antigravity."""
    briefing_lower = briefing.lower()

    types = {
        "Premium E-commerce": ["e-commerce", "loja", "shop", "carrinho", "venda"],
        "SaaS / Dashboard Admin": ["crm", "erp", "admin", "dashboard", "sistema", "plataforma"],
        "High-Conversion Landing Page": ["site", "website", "landing", "institucional"],
        "Scalable Backend API": ["api", "backend", "serviço", "endpoint", "microservice"],
        "Cross-Platform App": ["mobile", "app", "ios", "android"],
    }

    for ptype, keywords in types.items():
        if any(k in briefing_lower for k in keywords):
            return ptype
    return "Custom Scalable System"


def generate_plan(briefing: str, project_type: str, tech_stack: list = None) -> list:
    """Gera plano de execucao baseado no tipo de projeto e tecnologias."""
    if tech_stack is None:
        tech_stack = []

    # Monta tecnologias para o plano
    techs = " + ".join(tech_stack) if tech_stack else "Next.js + Prisma"

    plans = {
        "website": [
            f"1. Setup projeto {techs}",
            "2. Criar layout base (header, footer, hero)",
            "3. Implementar paginas (home, sobre, contato)",
            "4. Adicionar styling e responsividade",
            "5. Deploy e testes",
        ],
        "webapp": [
            f"1. Setup projeto com {techs}",
            "2. Definir schema do banco de dados",
            "3. Criar API routes e controllers",
            "4. Implementar UI com componentes",
            "5. Adicionar autenticacao",
            "6. Deploy e testes",
        ],
        "api": [
            "1. Setup API com FastAPI/Express",
            "2. Definir models e schemas",
            "3. Criar endpoints REST",
            "4. Implementar validacoes",
            "5. Adicionar autenticacao",
            "6. Deploy e testes",
        ],
        "ecommerce": [
            f"1. Setup Next.js com {techs}",
            "2. Criar schema produtos/pedidos",
            "3. Implementar checkout",
            "4. Criar dashboard admin",
            "5. Adicionar sistema de pagamento",
            "6. Deploy",
        ],
    }
    return plans.get(project_type, plans["webapp"])


def main():
    if len(sys.argv) < 2:
        print('Usage: python auto_rag.py "seu briefing aqui"')
        print("\nExample:")
        print(
            '  python auto_rag.py "Criar um site de entregas de comida com pedidos online"'
        )
        sys.exit(1)

    briefing = " ".join(sys.argv[1:])
    result = auto_plan_and_execute(briefing)

    print("\n" + "=" * 60)
    print(">>> PLANO DE PROJETO")
    print("=" * 60)
    print(f"\n[Tipo]: {result['project_type']}")
    print(f"[Tech Stack]: {', '.join(result['tech_stack'])}")
    print("\n[Plano de Execucao]:")
    for step in result["plan"]:
        print(f"  {step}")

    print("\n" + "-" * 60)
    print("[CONTEXTO OTIMIZADO - use no seu agente]:")
    print("-" * 60)
    print(result["context"][:1000] + "...")


if __name__ == "__main__":
    main()
