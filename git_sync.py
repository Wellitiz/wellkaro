import subprocess
import time
from pathlib import Path
from knowledge_distiller import distill_knowledge
from historian import generate_session_summary

def run_git_sync(message=None):
    """Executa a sincronização automática com o GitHub v6.0."""
    
    # --- NOVO: Ciclo de Consciência Antigravity v6.0 ---
    print("[*] Iniciando Ciclo de Consciência v6.0...")
    
    # 1. Destilação de Conhecimento (Aprendizado)
    distill_knowledge()
    
    # 2. Historiador de Sessão (Auto-Documentação)
    generate_session_summary()
    
    if message is None:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        message = f"Antigravity v6.0 - Full Sync: {timestamp}"
    
    print(f"[*] Sincronizando com GitHub...")
    
    try:
        # 3. Git Add
        print("[*] git add .")
        subprocess.run(["git", "add", "."], check=True)
        
        # 4. Git Commit
        print(f"[*] git commit -m '{message}'")
        subprocess.run(["git", "commit", "-m", message], check=False)
        
        # 5. Git Push
        print("[*] git push origin main")
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print(f"\n[OK] Antigravity v6.0 (Consciência Plena) sincronizado com sucesso!")
        return True
    except Exception as e:
        print(f"\n[!] Erro na sincronização v6.0: {e}")
        return False

if __name__ == "__main__":
    run_git_sync()
