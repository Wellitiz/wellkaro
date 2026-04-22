"""
🎯 Auto-Executor: Camada de Execução Automática do Antigravity v5.1

Este módulo intercepta prompts do usuário e executa automaticamente
comandos quando detecta trigger words específicas.

Uso:
    auto_executor.process("make a video") → executa npx create-video
    auto_executor.process("run SEO audit") → executa /seo audit
"""

import subprocess
import re
from pathlib import Path
from typing import Optional, Tuple

# Mapping de triggers → comandos
AUTO_TRIGGERS = {
    # Remotion (Vídeo)
    "make a video": "npx create-video",
    "create video": "npx create-video",
    "fazer um vídeo": "npx create-video",
    "video for": "npx create-video",
    "remotion": "remotion dev",
    "/remotion": "remotion dev",
    "build video": "remotion build",
    
    # Claude SEO
    "seo audit": "/seo audit",
    "audit SEO": "/seo audit",
    "seo report": "/seo google report full",
    "google report": "/seo google report",
    "page speed": "/seo google",
    "pagespeed": "/seo google",
    "geo": "/seo geo",
    "ai search": "/seo geo",
    "drift": "/seo drift baseline",
    
    # Marketing
    "landing page": "copy optimization",
    "convers": "CRO optimization",
    "copywriting": "copywriting AIDA",
    "cold email": "cold email sequence",
    "email sequence": "email sequence",
    "ab test": "ab-test-setup",
    
    # Superpowers
    "build": "brainstorming",
    "criar": "brainstorming", 
    "construir": "brainstorming",
    "debug": "systematic-debugging",
    "bug here": "systematic-debugging",
    "test first": "test-driven-development",
    "finish": "finishing-branch",
    "merge": "finishing-branch",
    
    # AI/Context
    "compress": "context compression",
    "reduce token": "context compression",
    "notebooklm": "notebooklm integration",
    "source grounded": "notebooklm integration",
    "subir para o git": "python git_sync.py",
    "git sync": "python git_sync.py",
}

# Comandos que precisam de argumento adicional
DYNAMIC_TRIGGERS = {
    "/seo geo": lambda url: f"/seo geo {url}",
    "/seo audit": lambda url: f"/seo audit {url}",  
    "/seo google report": lambda type: f"/seo google report {type}",
    "/seo drift baseline": lambda url: f"/seo drift baseline {url}",
    "/seo drift compare": lambda url: f"/seo drift compare {url}",
    "/remotion": lambda cmd: f"/remotion {cmd}",
}


def extract_url(prompt: str) -> Optional[str]:
    """Extrai URLs do prompt."""
    url_pattern = r'https?://[^\s]+'
    match = re.search(url_pattern, prompt)
    return match.group(0) if match else None


def process(prompt: str) -> Tuple[bool, str]:
    """
    Processa o prompt e retorna (needs_execution, command)
    
    Args:
        prompt: O prompt original do usuário
        
    Returns:
        (True, command) se deve executar automaticamente
        (False, "") se não há trigger
    """
    prompt_lower = prompt.lower()
    
    # 1. Check for Dynamic Triggers (com argumentos)
    for trigger, func in DYNAMIC_TRIGGERS.items():
        if trigger in prompt_lower:
            # Tenta extrair URL/argumento do prompt
            url = extract_url(prompt)
            if url:
                return True, func(url)
            # Se é tipo que precisa de tipo
            if "report" in prompt_lower and "full" not in prompt_lower:
                return True, "/seo google report full"
            return True, func("")  # Retorna base command
    
    # 2. Check for Static Triggers
    for trigger, command in AUTO_TRIGGERS.items():
        if trigger in prompt_lower:
            return True, command
    
    # 3. Sem trigger - retornar False
    return False, ""


def execute_command(command: str) -> Tuple[bool, str]:
    """
    Executa o comando via subprocess.
    
    Args:
        command: Comando a executar
        
    Returns:
        (success, output)
    """
    if not command:
        return False, "No command to execute"
    
    try:
        # Detectar tipo de comando
        if command.startswith("/"):
            # Comando interno do Antigravity (não executável via shell)
            return True, f"[AUTO-TRIGGER] → {command}"
        
        elif command.startswith("npx") or command.startswith("npm"):
            # Comando Node.js
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=60
            )
            return result.returncode == 0, result.stdout[:500] if result.stdout else result.stderr[:500]
        
        elif command == "remotion dev":
            # Development server
            result = subprocess.run(
                "remotion dev",
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            return True, "[Remotion Dev Server] Started on http://localhost:3000"
        
        elif command == "remotion build":
            result = subprocess.run(
                "remotion build",
                shell=True,
                capture_output=True,
                text=True,
                timeout=120
            )
            return True, f"[Remotion Build] {result.stdout[:200]}" if result.stdout else f"[Erro] {result.stderr[:200]}"
        
        elif command.startswith("python "):
            # Comando Python
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=120
            )
            return result.returncode == 0, result.stdout if result.stdout else result.stderr
        
        else:
            return True, f"[Command] {command}"
            
    except subprocess.TimeoutExpired:
        return True, f"[Timeout] {command}"
    except Exception as e:
        return False, f"[Error] {str(e)}"


# Teste rápido
if __name__ == "__main__":
    test_prompts = [
        "make a video for my product",
        "run SEO audit on https://example.com",
        "I need to debug this bug",
        "optimize my landing page conversions"
    ]
    
    print("=" * 60)
    print("TESTE AUTO-EXECUTOR")
    print("=" * 60)
    
    for prompt in test_prompts:
        needs_exec, cmd = process(prompt)
        print(f"\n[*] Input: {prompt}")
        print(f"    Trigger: {'YES' if needs_exec else 'NO'}")
        if needs_exec:
            print(f"    Command: {cmd}")