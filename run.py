#!/usr/bin/env python3
"""
Ativador Automatico do Sistema RAG
Executa automaticamente ao iniciar um projeto.
 Uso:
   python run.py "briefing do projeto"

   # Ou simplesmente:
   python run.py
   # E digite o briefing interativamente
"""

import sys
from pathlib import Path
import auto_rag
import auto_executor


def main():
    print("=" * 60)
    print(">>> ANTIGRAVITY AUTO-PLANNER")
    print("=" * 60)
    print("\n Este sistema analisa seu briefing e cria um plano")
    print(" otimizado com os melhores agentes e skills.\n")

    if len(sys.argv) > 1:
        briefing = " ".join(sys.argv[1:])
    else:
        print("Digite o briefing do seu projeto:")
        print("(Ex: Criar um sistema de delivery com Next.js, Prisma e Stripe)")
        print()
        briefing = input("> ")

    if not briefing.strip():
        print("Erro: Briefing vazio")
        sys.exit(1)

    # --- NOVO: Autonomous Bridge v5.2 ---
    needs_action, command = auto_executor.process(briefing)
    
    if needs_action:
        print("\n" + "!" * 60)
        print(f">>> GATILHO DETECTADO: {command}")
        print("!" * 60)
        print("\nEste briefing parece ser uma acao direta e nao apenas um projeto.")
        confirm = input(f"Deseja EXECUTAR o comando agora? (s/n): ").lower()
        
        if confirm == 's':
            success, output = auto_executor.execute_command(command)
            print(f"\n[OUTPUT]:\n{output}")
            
            cont = input("\nDeseja prosseguir TAMBEM com o planejamento de RAG? (s/n): ").lower()
            if cont != 's':
                print("\nEncerrando Bridge Autônoma. Até logo, Comandante.")
                sys.exit(0)

    # Executa o planejamento automatico (Fluxo Normal)
    result = auto_rag.auto_plan_and_execute(briefing)

    # Exibe resultado formatado
    print("\n" + "=" * 60)
    print(">>> PLANO DE PROJETO")
    print("=" * 60)
    print(f"\n[Tipo]: {result['project_type']}")
    print(f"[Tech Stack]: {', '.join(result['tech_stack'])}")
    print("\n[Plano de Execucao]:")
    for step in result["plan"]:
        print(f"  {step}")

    print("\n" + "-" * 60)
    print("[CONTEXTO OTIMIZADO]:")
    print("-" * 60)
    print(result["context"])
    print("\n" + "=" * 60)
    print(">>> Copie o contexto acima e use no seu agente AI")
    print("=" * 60)


if __name__ == "__main__":
    main()
