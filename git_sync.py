import subprocess
import time
from pathlib import Path

def run_git_sync(message=None):
    """Executa a sincronização automática com o GitHub."""
    if message is None:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        message = f"Auto Update v5.1 - Sync: {timestamp}"
    
    print(f"[*] Iniciando Sincronização Antigravity para o Git...")
    
    try:
        # 1. Git Add
        print("[*] git add .")
        subprocess.run(["git", "add", "."], check=True)
        
        # 2. Git Commit
        print(f"[*] git commit -m '{message}'")
        subprocess.run(["git", "commit", "-m", message], check=False) # Pode falhar se não houver mudanças
        
        # 3. Git Push
        print("[*] git push origin main")
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print(f"\n[OK] Antigravity v5.1 sincronizado com sucesso no GitHub!")
        return True
    except Exception as e:
        print(f"\n[!] Erro durante a sincronização: {e}")
        return False

if __name__ == "__main__":
    run_git_sync()
