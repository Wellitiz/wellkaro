"""
🎯 Auto-Executor CLI - Interface de Linha de Comando

Uso:
    python auto_executor_cli.py "make a video"
    python auto_executor_cli.py "run SEO audit on https://example.com"
    
Também pode ser importado como módulo:
    from auto_executor_cli import run_auto
    run_auto("seu prompt aqui")
"""

import sys
from pathlib import Path

# Adiciona o diretório atual ao path
sys.path.insert(0, str(Path(__file__).parent))

from auto_executor import process, execute_command


def run_auto(prompt: str, verbose: bool = True):
    """
    Executa automaticamente baseado no prompt.

    Args:
        prompt: O comando/prompt do usuário
        verbose: Se True, mostra o output detalhado

    Returns:
        dict com {needs_exec, command, success, output}
    """
    if verbose:
        print("=" * 60)
        print(f"[*] PROCESSANDO: {prompt}")
        print("=" * 60)
    
    needs_exec, auto_cmd = process(prompt)

    if not needs_exec:
        if verbose:
            print("[!] Nenhum trigger encontrado")
        return {"needs_exec": False, "command": None, "success": False, "output": "No trigger found"}

    if verbose:
        print(f"[*] TRIGGER DETECTADO: {auto_cmd}")
        print(f"[*] EXECUTANDO: {auto_cmd}")
    
    # Executa o comando
    success, output = execute_command(auto_cmd)
    
    result = {
        "needs_exec": needs_exec,
        "command": auto_cmd,
        "success": success,
        "output": output[:500] if output else ""
    }

    if verbose:
        print("-" * 60)
        if success:
            print(f"[OK] SUCESSO: {output[:200]}")
        else:
            print(f"[!] RESULTADO: {output[:200]}")
    
    return result


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Uso: python auto_executor_cli.py '<seu comando>'")
        print("Exemplos:")
        print("  python auto_executor_cli.py 'make a video'")
        print("  python auto_executor_cli.py 'run SEO audit on https://example.com'")
        print("  python auto_executor_cli.py 'I need to debug this bug'")
        sys.exit(1)
    
    prompt = " ".join(sys.argv[1:])
    run_auto(prompt)


if __name__ == "__main__":
    main()