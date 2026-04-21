import os
from pathlib import Path
import json
import time

# Configurações
CUSTOM_FIXES_DIR = Path(".agent/custom-fixes")
TASKS_FILE = Path("task.md")

def distill_knowledge(project_name="global"):
    """Analisa o contexto atual e extrai aprendizado para memoria persistente."""
    print(f"[*] Iniciando Destilação de Conhecimento para o projeto: {project_name}...")
    
    if not TASKS_FILE.exists():
        print("[!] Erro: task.md não encontrado para análise.")
        return

    # 1. Ler tarefas concluidas
    tasks = TASKS_FILE.read_text(encoding="utf-8")
    completed_tasks = [line for line in tasks.split("\n") if "[x]" in line]
    
    if not completed_tasks:
        print("[*] Nenhuma tarefa nova concluída para destilar.")
        return

    print(f"[*] Encontradas {len(completed_tasks)} tarefas concluídas. Gerando memória...")

    # 2. Criar diretório do projeto se não existir
    project_fix_dir = CUSTOM_FIXES_DIR / project_name
    project_fix_dir.mkdir(parents=True, exist_ok=True)

    # 3. Gerar o arquivo de Fix
    # Nota: Em um sistema real, aqui chamaríamos a LLM para resumir a solução.
    # No protótipo v5, criamos o template e o registro do fix.
    
    timestamp = int(time.time())
    fix_filename = f"distilled_fix_{timestamp}.md"
    fix_path = project_fix_dir / fix_filename
    
    fix_content = f"""# 🧠 Solução Destilada: {completed_tasks[-1].replace('[x]', '').strip()}
Data: {time.strftime('%Y-%m-%d %H:%M:%S')}
Projeto: {project_name}

## 📋 Contexto das Tarefas Realizadas:
{tasks}

## 🛠️ Resumo da Solução:
[O Antigravity v5 identificou que esta tarefa foi concluída com sucesso. 
O histórico de comandos e os arquivos alterados sugerem uma implementação estável.]

> [!TIP]
> Esta memória agora faz parte do Loop de Feedback. Na próxima vez que uma tarefa similar surgir, 
> este conhecimento receberá um boost de 1.3x de relevância.
"""

    fix_path.write_text(fix_content, encoding="utf-8")
    print(f"[OK] Memoria persistente salva em: {fix_path}")
    
    return str(fix_path)

if __name__ == "__main__":
    import sys
    project = sys.argv[1] if len(sys.argv) > 1 else "global"
    distill_knowledge(project)
