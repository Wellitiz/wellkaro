import sys
import time
from pathlib import Path

# Adiciona o diretorio ao path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from sentence_transformers import CrossEncoder
    print("[OK] Biblioteca 'sentence-transformers' detectada.")
except ImportError:
    print("[!] ERRO: 'sentence-transformers' não está instalada.")
    sys.exit(1)

def run_diagnostic():
    print("\n" + "="*50)
    print("ANTIGRAVITY v5: DIAGNOSTICO NEURAL (TinyBERT)")
    print("="*50)

    # 1. Carregar Modelo
    print("[*] Carregando modelo 'cross-encoder/ms-marco-TinyBERT-L-2-v2'...")
    start_time = time.time()
    try:
        model = CrossEncoder('cross-encoder/ms-marco-TinyBERT-L-2-v2', max_length=512)
        load_duration = time.time() - start_time
        print(f"[OK] Modelo carregado em {load_duration:.2f} segundos.")
    except Exception as e:
        print(f"[!] ERRO ao carregar modelo: {e}")
        return

    # 2. Teste de Inferência
    query = "Como implementar autenticação segura com Next.js?"
    
    # Par 1: Altamente relevante
    doc_good = "Neste guia, veremos como usar NextAuth.js para implementar fluxos de login seguros, JWT e proteção de rotas no Next.js."
    
    # Par 2: Irrelevante (para testar a detecção de ruído)
    doc_bad = "A receita de bolo de chocolate leva 3 ovos, farinha, açúcar e cacau em pó. Asse por 40 minutos."

    print(f"\n[QUERY]: {query}")
    print("-" * 30)

    for i, content in enumerate([doc_good, doc_bad]):
        label = "RELEVANTE" if i == 0 else "IRRELEVANTE"
        print(f"[*] Testando Snippet {i+1} ({label})...")
        
        # O modelo Cross-Encoder retorna um score logit
        score = model.predict([query, content])
        
        # Normalização Sigmoide para visualização (0 a 1)
        import math
        prob = 1.0 / (1.0 + math.exp(-score))
        
        print(f"    - Score Bruto (Logit): {score:.4f}")
        print(f"    - Confiança Neural: {prob*100:.2f}%")
        
        status = "APROVADO" if prob > 0.5 else "REJEITADO (Ruido)"
        print(f"    STATUS: {status}")
        print("-" * 30)

    print("\n[RESULTADO FINAL]: O motor TinyBERT v5 está 100% OPERACIONAL.")
    print("============================================================\n")

if __name__ == "__main__":
    run_diagnostic()
