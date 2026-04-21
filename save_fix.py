import sys
import os
from pathlib import Path

def save_fix(project_name: str, title: str, description: str):
    """
    Utilitário para o Feedback Loop do Antigravity v4.
    Salva uma solução técnica na base de conhecimento para uso futuro.
    """
    base_dir = Path(".agent/custom-fixes")
    project_dir = base_dir / project_name
    
    if not project_dir.exists():
        project_dir.mkdir(parents=True, exist_ok=True)
    
    # Sanitizar nome do arquivo
    file_name = title.lower().replace(" ", "_").replace("/", "_") + ".md"
    file_path = project_dir / file_name
    
    content = f"""# Solução: {title}
Projeto: {project_name}
Tipo: Feedback Loop / Custom Fix

## Contexto
{description}

---
*Indexado automaticamente pelo Antigravity Core v4*
"""
    
    file_path.write_text(content, encoding="utf-8")
    print(f"[OK] Solução salva em: {file_path}")
    print("[*] O motor irá indexar esta correção na próxima interação.")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: python save_fix.py \"Nome do Projeto\" \"Título da Correção\" \"Descrição da Solução\"")
        sys.exit(1)
        
    p_name = sys.argv[1]
    title = sys.argv[2]
    desc = sys.argv[3]
    
    save_fix(p_name, title, desc)
