import chromadb
import os

def check_chroma_count():
    # Caminho real na raiz do projeto Antigravity
    persist_directory = r"C:\Users\welli\Downloads\Antigravity\chroma_db"
    
    if not os.path.exists(persist_directory):
        print(f"Diretório não encontrado: {persist_directory}")
        return

    # Usando o cliente para o diretório de persistência
    client = chromadb.PersistentClient(path=persist_directory)
    
    try:
        collections = client.list_collections()
        total_docs = 0
        
        print(f"--- Relatório de Indexação ChromaDB (v6.6) ---")
        if not collections:
            print("Nenhuma coleção encontrada.")
        
        for col in collections:
            count = col.count()
            print(f"Coleção: {col.name} | Documentos: {count}")
            total_docs += count
            
        print(f"---------------------------------------")
        print(f"TOTAL DE DOCUMENTOS INDEXADOS: {total_docs}")
    except Exception as e:
        print(f"Erro ao acessar ChromaDB: {e}")

if __name__ == "__main__":
    check_chroma_count()
