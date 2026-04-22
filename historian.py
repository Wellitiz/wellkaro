import subprocess
import time
from pathlib import Path

# Configurações Antigravity v6.0
SESSAO_FILE = Path("SESSAO.md")
WALKTHROUGH_FILE = Path("walkthrough.md")
TASK_FILE = Path("task.md")

def get_git_diff():
    """Captura o diff da sessão atual."""
    try:
        # Pega as mudanças que ainda não foram para o remote (ou desde o último commit)
        result = subprocess.run(["git", "diff", "HEAD"], capture_output=True, text=True)
        return result.stdout if result.stdout else "Nenhuma mudança de código detectada."
    except Exception:
        return "Erro ao capturar Git diff."

def get_completed_tasks():
    """Lê as tarefas concluídas no task.md."""
    if not TASK_FILE.exists():
        return "Nenhum arquivo task.md encontrado."
    
    content = TASK_FILE.read_text(encoding="utf-8")
    completed = [line.replace("[x]", "✅").strip() for line in content.split("\n") if "[x]" in line]
    return "\n".join(completed) if completed else "Nenhuma tarefa marcada como concluída."

def generate_session_summary():
    """Gera o resumo técnico da sessão v6.0."""
    print("[*] Historiano v6.0: Analisando rastros da sessão...")
    
    diff = get_git_diff()
    tasks = get_completed_tasks()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Template do Historiano (Em v6.0 real, isso passaria pela LLM para refinamento)
    historian_report = f"""# 📜 Relatório do Historiano v6.0
**Data:** {timestamp}

## 🎯 Atividades Executadas
{tasks}

## 🛠️ Mudanças Técnicas (Resumo do Diff)
```diff
{diff[:1000]}...
```

---
> [Auto-Documented by Antigravity v6.0 Historian]
"""
    
    # 1. Update SESSAO.md (Append)
    if SESSAO_FILE.exists():
        old_content = SESSAO_FILE.read_text(encoding="utf-8")
        SESSAO_FILE.write_text(historian_report + "\n\n" + old_content, encoding="utf-8")
    else:
        SESSAO_FILE.write_text(historian_report, encoding="utf-8")
    
    print(f"[OK] SESSAO.md atualizada pelo Historiano.")
    
    # 2. Update walkthrough.md (Overwrite com o estado atual do progresso)
    WALKTHROUGH_FILE.write_text(f"""# Walkthrough Atualizado: {timestamp}
    
Esta sessão focou na implementação de ferramentas de consciência v6.0.

## Conquistas da Sessão:
{tasks}

---
*Gerado automaticamente pelo Historiano Antigravity.*
""", encoding="utf-8")
    
    print(f"[OK] walkthrough.md atualizado pelo Historiano.")

if __name__ == "__main__":
    generate_session_summary()
