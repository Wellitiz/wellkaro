import os
import sys
import chromadb
from chromadb.config import Settings
from pathlib import Path

AGENTS_DIR = Path(".agent")
PROJETOS_DIR = Path("Projetos")
CHROMA_PATH = "./chroma_db"
BATCH_SIZE = 100

AGENT_KEYWORDS = [
    "expert", "agent", "specialist", "engineer", "architect",
    "consultant", "developer", "manager", "officer", "pro",
    "master", "sensei", "guru", "analyst", "strategist",
    "designer", "tester", "security", "devops", "fullstack",
    "backend", "frontend", "lead", "senior"
]

# Extensoes que realmente importam para o contexto logico e arquitetural
CODE_EXTENSIONS = [".ts", ".tsx", ".prisma", ".py", ".md", ".js"]


def get_categories_from_path(file_path: Path) -> list[str]:
    """Extrai categorias do caminho hierarquico dentro de .agent."""
    parts = file_path.parts
    if ".agent" in parts:
        idx = parts.index(".agent")
        # Se houver algo entre .agent e o diretorio da skill, sao categorias
        # Ex: .agent/frontend,mobile/react-expert/SKILL.md -> parts[idx+1] e "frontend,mobile"
        if len(parts) > idx + 2:
            cat_part = parts[idx + 1]
            return [c.strip() for c in cat_part.split(",") if c.strip()]
    return ["uncategorized"]


def classify_document(folder_name: str, file_path: Path) -> str:
    """Classifica o documento como 'agent', 'skill', 'code', 'fix' ou 'ki'."""
    path_str = str(file_path).replace("\\", "/")
    
    if "custom-fixes" in path_str:
        return "fix"
    if "local-kis" in path_str:
        return "ki"
    if "Projetos" in path_str:
        return "code"
    
    # Busca keywords no nome da pasta da skill ou nas categorias
    search_context = folder_name.lower()
    categories = get_categories_from_path(file_path)
    search_context += " " + " ".join(categories).lower()

    for keyword in AGENT_KEYWORDS:
        if keyword in search_context:
            return "agent"
    return "skill"


def get_project_name(file_path: Path) -> str:
    """Identifica o nome do projeto baseado no caminho (Projetos, local-kis ou custom-fixes)."""
    parts = file_path.parts
    
    # 1. Padrao: Projetos/NomeProjeto
    if "Projetos" in parts:
        idx = parts.index("Projetos")
        if len(parts) > idx + 1:
            return parts[idx + 1]
            
    # 2. Padrao: .agent/local-kis/NomeProjeto
    if "local-kis" in parts:
        idx = parts.index("local-kis")
        if len(parts) > idx + 1:
            return parts[idx + 1]
            
    # 3. Padrao: .agent/custom-fixes/NomeProjeto
    if "custom-fixes" in parts:
        idx = parts.index("custom-fixes")
        if len(parts) > idx + 1:
            return parts[idx + 1]
            
    return "global"


def get_files_to_index(directory: Path) -> list[Path]:
    """Retorna lista de caminhos de arquivos suportados, focando em diretorios de codigo e docs."""
    files_to_index = []
    if not directory.exists():
        return []

    # Pastas que sempre ignoramos
    exclude_dirs = {
        "node_modules", ".next", ".git", "dist", "build", "__pycache__",
        ".venv", "env", "venv", "target", "out", "chroma_db",
        ".ruff_cache", "public", "assets", ".expo", ".serverless",
        "vendor", "libs", "library"
    }
    
    # Pastas que priorizamos em projetos (se existirem, so olhamos nelas)
    priority_dirs = {"src", "app", "lib", "prisma", "pages", "components", "services", "api"}
    
    exclude_dirs_lower = {d.lower() for d in exclude_dirs}
        
    for root, dirs, files in os.walk(directory):
        rel_path = Path(root).relative_to(directory)
        
        # Filtro de descida: ignorar pastas ruidosas
        dirs[:] = [d for d in dirs if d.lower() not in exclude_dirs_lower]
        
        # Feedback visual de varredura
        if len(files_to_index) % 100 == 0:
            print(f"  [>] Varrendo: {rel_path} ({len(files_to_index)} arquivos encontrados...)")
        
        # Estrategia Cirurgica: se estivermos na raiz de um projeto, 
        # priorizamos certas pastas e ignoramos o resto da raiz (exceto .md)
        is_project_root = len(rel_path.parts) == 1 and directory == PROJETOS_DIR
        
        for file in files:
            path = Path(root) / file
            ext = path.suffix.lower()
            
            # Sempre indexamos .md
            if ext == ".md":
                files_to_index.append(path)
                continue
                
            # Para outros arquivos de codigo, verificamos se estao em pastas de interesse
            if ext in CODE_EXTENSIONS:
                # Se for projeto, so indexamos se estiver em priority_dirs
                if "Projetos" in str(path):
                    if any(p in path.parts for p in priority_dirs):
                        files_to_index.append(path)
                else:
                    # Se for global (.agent), indexamos tudo dentro das extensoes permitidas
                    files_to_index.append(path)
                
    return files_to_index


def read_file_content(file_path: Path) -> str | None:
    """Le o conteudo do arquivo com fallback de encoding."""
    encodings = ["utf-8", "utf-8-sig", "latin-1", "cp1252"]
    for encoding in encodings:
        try:
            return file_path.read_text(encoding=encoding)
        except (UnicodeDecodeError, OSError):
            continue
    return None


def index_all() -> dict:
    """Indexa skills globais (.agent) e projetos locais (Projetos/)."""
    try:
        print("[*] Antigravity Core v4: Iniciando Indexacao...")
        
        print(f"[*] Acessando banco em: {CHROMA_PATH}")
        client = chromadb.PersistentClient(
            path=CHROMA_PATH, settings=Settings(anonymized_telemetry=False)
        )
        print("[*] Cliente ChromaDB inicializado.")

        collection = client.get_or_create_collection(
            name="skills_rag", metadata={"hnsw:space": "cosine"}
        )
        print(f"[*] Colecao 'skills_rag' acessada. Total atual: {collection.count()} documentos.")

        print("[*] Varrendo diretorios...")
        all_files = get_files_to_index(AGENTS_DIR) + get_files_to_index(PROJETOS_DIR)
        print(f"[*] Total de arquivos encontrados para analise: {len(all_files)}")

        documents = []
        ids = []
        metadatas = []
        seen_ids = set()

        for i, file_path in enumerate(all_files):
            content = read_file_content(file_path)
            if not content or len(content.strip()) < 10:
                continue

            project_name = get_project_name(file_path)
            folder_name = file_path.parent.name
            doc_type = classify_document(folder_name, file_path)
            categories = get_categories_from_path(file_path)
            
            # ID unico baseado no caminho relativo para evitar duplicatas e permitir atualizacao
            relative_path = str(file_path).replace("\\", "/")
            doc_id = f"v4_{relative_path}"
            
            if doc_id in seen_ids:
                continue
            seen_ids.add(doc_id)

            # 8.000 caracteres e ideal
            documents.append(content[:8000])
            ids.append(doc_id)
            metadatas.append({
                "type": doc_type,
                "project": project_name,
                "file_name": file_path.name,
                "file_path": relative_path,
                "folder": folder_name,
                "categories": ",".join(categories) # ChromaDb nao aceita listas, usamos string separada por virgula
            })

            if len(documents) >= 100:
                print(f"  [>] Enviando lote de {len(documents)} documentos para o banco...")
                collection.upsert(documents=documents, ids=ids, metadatas=metadatas)
                print(f"  [OK] Lote processado ({i+1}/{len(all_files)} files).")
                documents, ids, metadatas = [], [], []
                import time
                time.sleep(0.1)

        if documents:
            print(f"  [>] Enviando lote final de {len(documents)} documentos...")
            collection.upsert(documents=documents, ids=ids, metadatas=metadatas)
            print("  [OK] Lote final processado.")

        print("\n[*] Indexacao concluida com sucesso!")
        print(f"[*] Total no ChromaDB: {collection.count()} documentos.")
        
        return {"total": collection.count()}
    except Exception as e:
        import traceback
        print(f"[!] ERRO CRITICO NA INDEXACAO: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    index_all()
