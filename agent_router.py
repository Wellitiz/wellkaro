import chromadb
from chromadb.config import Settings
from pathlib import Path
from typing import TypedDict, Optional
import json
import time
import os

# Neural Engine Dependencies
try:
    from sentence_transformers import CrossEncoder
    HAS_NEURAL = True
except ImportError:
    HAS_NEURAL = False

CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "skills_rag"
CONSCIENCE_LOG = Path("antigravity_conscience.log")

# Model Singleton
_RERANKER_MODEL = None


class RetrievalResult(TypedDict):
    agents: list[dict]
    skills: list[dict]
    code: list[dict]
    fixes: list[dict]
    kis: list[dict]


# Singleton para conexões persistentes no Windows
_CHROMA_CLIENT = None
_CHROMA_COLLECTION = None


def get_reranker():
    """Retorna o modelo de Reranker (Singleton)."""
    global _RERANKER_MODEL
    if HAS_NEURAL and _RERANKER_MODEL is None:
        log_event("system", {"msg": "Carregando motor neural v5 (Reranker)..."})
        # Usamos um modelo ultra-rapido e preciso para ambiente local
        # O download ocorre apenas na primeira execução (~100MB)
        _RERANKER_MODEL = CrossEncoder('cross-encoder/ms-marco-TinyBERT-L-2-v2', max_length=512)
        log_event("system", {"msg": "Motor neural v5 carregado com sucesso."})
    return _RERANKER_MODEL


def get_client() -> chromadb.PersistentClient:
    """Retorna o cliente ChromaDB (Singleton)."""
    global _CHROMA_CLIENT
    if _CHROMA_CLIENT is None:
        _CHROMA_CLIENT = chromadb.PersistentClient(
            path=CHROMA_PATH, settings=Settings(anonymized_telemetry=False)
        )
    return _CHROMA_CLIENT

def get_collection() -> chromadb.Collection:
    """Retorna a colecao de skills (Singleton). Sincronizacao automatica v4 ativada."""
    global _CHROMA_COLLECTION
    if _CHROMA_COLLECTION is None:
        check_and_reindex()
        client = get_client()
        _CHROMA_COLLECTION = client.get_or_create_collection(
            name=COLLECTION_NAME, metadata={"hnsw:space": "cosine"}
        )
    return _CHROMA_COLLECTION


def check_and_reindex():
    """Verifica se ha mudancas na pasta .agent ou Projetos e re-indexa se necessario."""
    import os
    import time
    from index_skills import index_all
    
    # Monitoramos .agent e Projetos para mudancas
    paths_to_watch = [Path(".agent"), Path("Projetos")]
    state_file = Path(".agent_last_sync")
    
    current_max_mtime = 0
    for p in paths_to_watch:
        if p.exists():
            current_max_mtime = max(current_max_mtime, os.path.getmtime(p))
            # Checagem rasa de subpastas para novos projetos
            for item in p.iterdir():
                if item.is_dir():
                    current_max_mtime = max(current_max_mtime, os.path.getmtime(item))
                
    last_sync = 0
    if state_file.exists():
        try:
            last_sync = float(state_file.read_text())
        except ValueError:
            last_sync = 0
        
    if current_max_mtime > last_sync:
        print("[!] Mudancas ou novos projetos detectados. Sincronizando base de conhecimento v4...")
        index_all()
        state_file.write_text(str(time.time()))


def log_event(event_type: str, data: dict):
    """Registra um evento para o Monitor de Consciencia."""
    log_entry = {
        "timestamp": time.time(),
        "event": event_type,
        "data": data
    }
    with open(CONSCIENCE_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")


def expand_query(query: str) -> list[str]:
    """Expande a query para capturar mais nuances semanticas."""
    variations = [
        query,
        f"{query} architecture design patterns expert",
        f"{query} security audit best practices",
        f"{query} high-performance implementation premium"
    ]
    log_event("query_expansion", {"original": query, "variations": variations})
    return variations


def retrieve_documents(
    user_prompt: str, 
    project_name: Optional[str] = None,
    n_agents: int = 1, 
    n_skills: int = 2,
    n_code: int = 3
) -> RetrievalResult:
    """
    Executa busca vetorial com expansao de query, deduplicacao e filtragem de projeto.
    """
    collection = get_collection()
    queries = expand_query(user_prompt)

    # Filtro base: SEMPRE traz o conhecimento global
    # Se houver um projeto especifico, traz (global OR projeto)
    where_filter = {"project": "global"}
    if project_name and project_name != "global":
        where_filter = {"$or": [
            {"project": "global"},
            {"project": project_name}
        ]}

    def query_type(doc_type: str, n: int) -> list[dict]:
        if n <= 0: return []
        
        type_filter = {"type": doc_type}
        # Combina com o filtro de projeto se necessario
        final_where = {"$and": [where_filter, type_filter]} if project_name else type_filter
        
        results = collection.query(
            query_texts=queries,
            n_results=n * 2, # Busca um pouco mais para permitir reranking com boost
            where=final_where,
            include=["documents", "metadatas", "distances"],
        )
        
        dedup_dict = {}
        for i in range(len(queries)):
            if results["ids"] and results["ids"][i]:
                for j, doc_id in enumerate(results["ids"][i]):
                    base_score = 1 - results["distances"][i][j]
                    
                    # --- CONTEXT BOOSTING v4 ---
                    meta = results["metadatas"][i][j]
                    score = base_score
                    
                    # 1. Boost por Projeto Ativo (Prioridade maxima)
                    if project_name and meta.get("project") == project_name:
                        score *= 1.5
                    
                    # 2. Boost por Tipo de Solucao (Fixes e KIs locais)
                    if meta.get("type") in ["fix", "ki"]:
                        score *= 1.3

                    # 3. CONTEXTUAL CATEGORY BOOSTING (Novo v4)
                    doc_categories = meta.get("categories", "").lower().split(",")
                    query_lower = user_prompt.lower()
                    cat_boosted = False
                    for cat in doc_categories:
                        if cat != "uncategorized" and cat in query_lower:
                            score *= 1.2
                            cat_boosted = True
                            break # Aplica boost apenas uma vez por doc

                    if doc_id not in dedup_dict or score > dedup_dict[doc_id]["score"]:
                        log_event("hit", {
                            "type": doc_type,
                            "name": meta.get("file_name"),
                            "categories": doc_categories,
                            "base_score": base_score,
                            "final_score": score,
                            "project_boost": meta.get("project") == project_name,
                            "solution_boost": meta.get("type") in ["fix", "ki"],
                            "category_boost": cat_boosted
                        })
                        dedup_dict[doc_id] = {
                            "id": doc_id,
                            "name": meta.get("file_name") or meta.get("name", doc_id),
                            "file_path": meta.get("file_path", ""),
                            "project": meta.get("project", "global"),
                            "content": results["documents"][i][j],
                            "score": score,
                            "type": meta.get("type")
                        }
        
        # --- ETAPA DE RERANKING NEURAL v5 ---
        results_list = list(dedup_dict.values())
        reranker = get_reranker()
        
        if reranker and results_list:
            log_event("neural_rerank", {"count": len(results_list)})
            # Prepara pares (query, doc_content)
            pairs = [[user_prompt, doc["content"][:1000]] for doc in results_list]
            scores = reranker.predict(pairs)
            
            # Atualiza scores com fusão (50% contextual boost + 50% neural accuracy)
            for j, score in enumerate(scores):
                # Normaliza neural score para 0-1 (aproximadamente)
                neural_score = 1.0 / (1.0 + pow(2.71828, -score)) 
                results_list[j]["score"] = (results_list[j]["score"] * 0.5) + (neural_score * 0.5)
                results_list[j]["neural_score"] = float(neural_score)

        # Retorna os N melhores apos o boost e reranking
        final_sorted = sorted(results_list, key=lambda x: x["score"], reverse=True)[:n]
        return final_sorted

    return {
        "agents": query_type("agent", n_agents),
        "skills": query_type("skill", n_skills),
        "code": query_type("code", n_code),
        "fixes": query_type("fix", 2), # Traz ate 2 correcoes passadas se relevantes
        "kis": query_type("ki", 2)      # Traz ate 2 Knowledge Items locais
    }


def scan_file_dependencies(file_path: str, project_name: str = "global") -> dict:
    """
    Realiza uma varredura leve de dependências para o Graph Scan.
    Detecta imports, chamadas de funções e variáveis globais para calcular o Blast Radius.
    """
    import re
    from pathlib import Path
    
    impact_data = {
        "direct_imports": [],
        "possible_dependents": [],
        "risk_level": "low",
        "files_to_check": []
    }
    
    try:
        # Converte path para objeto Path
        path_obj = Path(file_path)
        if not path_obj.exists():
            return impact_data
        
        # Lê o conteúdo do arquivo
        content = path_obj.read_text(encoding="utf-8", errors="ignore")
        
        # Detecta linguagem pelo extensão
        ext = path_obj.suffix.lower()
        
        if ext in [".ts", ".tsx", ".js", ".jsx"]:
            # TypeScript/JavaScript: busca imports
            imports = re.findall(r"(?:import|from)\s+['\"]([^'\"]+)['\"]", content)
            impact_data["direct_imports"] = imports[:10]  # Limita a 10
            
            # Busca chamadas de funções comuns
            funcs = re.findall(r"(?:function\s+|const\s+|let\s+|var\s+)(\w+)\s*[=(:]", content)
            impact_data["functions_defined"] = funcs[:5]
            
        elif ext == ".py":
            # Python: busca imports
            imports = re.findall(r"^(?:from\s+(\S+)\s+import|import\s+(\S+))", content, re.MULTILINE)
            impact_data["direct_imports"] = [i[0] or i[1] for i in imports][:10]
            
        elif ext == ".prisma":
            # Prisma: busca models
            models = re.findall(r"model\s+(\w+)", content)
            impact_data["models_defined"] = models[:5]
        
        # Calcula risco baseado no tipo de arquivo
        high_risk_patterns = ["api", "controller", "service", "auth", "payment", "database"]
        if any(p in file_path.lower() for p in high_risk_patterns):
            impact_data["risk_level"] = "high"
        elif "component" in file_path.lower() or "page" in file_path.lower():
            impact_data["risk_level"] = "medium"
            
        # Lista arquivos para verificar (simulação do blast radius)
        parent_dir = str(path_obj.parent)
        impact_data["files_to_check"] = [
            f"{parent_dir}/index.ts",
            f"{parent_dir}/index.js", 
            f"{parent_dir}/module.ts",
            f"{parent_dir}/utils.ts"
        ]
        
    except Exception as e:
        log_event("graph_scan_error", {"file": file_path, "error": str(e)})
    
    return impact_data


def graph_scan(retrieval: RetrievalResult) -> dict:
    """
    Executa o Graph Scan após o TinyBERT reranking.
    Analisa dependências e calcula Blast Radius para cada arquivo recuperado.
    """
    scan_results = {
        "high_impact_files": [],
        "potential_issues": [],
        "files_to_review": [],
        "total_impact_score": 0
    }
    
    # Analisa todos os arquivos de código retornados
    for code_item in retrieval.get("code", []):
        file_path = code_item.get("file_path", "")
        project = code_item.get("project", "global")
        
        # Se for um arquivo de projeto (não global), faz a análise de dependências
        if project != "global" and file_path:
            deps = scan_file_dependencies(file_path, project)
            
            if deps.get("risk_level") in ["high", "medium"]:
                scan_results["high_impact_files"].append({
                    "file": file_path,
                    "risk": deps["risk_level"],
                    "imports": deps.get("direct_imports", [])[:3],
                    "score": code_item.get("score", 0)
                })
                scan_results["total_impact_score"] += 1 if deps["risk_level"] == "high" else 0.5
            
            if deps.get("files_to_check"):
                scan_results["files_to_review"].extend(deps["files_to_check"][:2])
    
    # Analisa skills e agents para potenciais conflitos
    for skill in retrieval.get("skills", []):
        skill_name = skill.get("name", "")
        if any(w in skill_name.lower() for w in ["security", "auth", "database"]):
            scan_results["potential_issues"].append({
                "type": "high_importance_skill",
                "name": skill_name,
                "advice": "Revisar com cuidado -skill de alto impacto"
            })
    
    log_event("graph_scan_complete", {
        "high_impact_count": len(scan_results["high_impact_files"]),
        "total_impact_score": scan_results["total_impact_score"]
    })
    
    return scan_results


def build_optimized_context(
    user_prompt: str, 
    project_name: Optional[str] = None,
    n_agents: int = 1, 
    n_skills: int = 2,
    n_code: int = 3
) -> str:
    """
    Constroi um contexto otimizado combinando agentes, skills e snippets de codigo do projeto.
    """
    # Busca normal de documentos
    retrieval = retrieve_documents(user_prompt, project_name, n_agents, n_skills, n_code)
    
    # --- ETAPA DE GRAPH SCAN v6.7 (Blast Radius Analysis) ---
    graph_analysis = graph_scan(retrieval)
    log_event("graph_scan", {"high_impact": len(graph_analysis.get("high_impact_files", []))})
    
    context_parts = []
    
    if project_name:
        context_parts.append(f"CONTEXTO DO PROJETO ATIVO: {project_name}\n")

    if retrieval["agents"]:
        context_parts.append(f"## EQUIPE DE ESPECIALISTAS SELECIONADA:")
        for agent in retrieval["agents"]:
            context_parts.append(f"- **{agent['name']}** (Retrieved from: {agent['file_path']})")

    if retrieval["skills"]:
        context_parts.append(f"\n## CONHECIMENTO TECNICO (SKILLS):")
        for skill in retrieval["skills"]:
            context_parts.append(f"- **{skill['name']}**: Referencia em {skill['file_path']}")

    if retrieval["kis"]:
        context_parts.append(f"\n## KNOWLEDGE ITEMS LOCAIS (REGRAS DO PROJETO):")
        for ki in retrieval["kis"]:
            context_parts.append(f"### {ki['name']} (Origem: {ki['file_path']})")
            context_parts.append(ki["content"])

    if retrieval["fixes"]:
        context_parts.append(f"\n## HISTORICO DE SOLUCOES (FEEDBACK LOOP):")
        for fix in retrieval["fixes"]:
            context_parts.append(f"### CORRECAO: {fix['name']}")
            context_parts.append(fix["content"])

    if retrieval["code"]:
        context_parts.append(f"\n## CONTEXTO DE CODIGO DO PROJETO (SNIPPETS):")
        for code in retrieval["code"]:
            context_parts.append(f"### Arquivo: {code['file_path']} (Score Boosted: {code['score']:.2f})")
            context_parts.append("```")
            context_parts.append(code["content"][:2000] + "...")  # Limit snippet size
            context_parts.append("```\n")

    # --- BLAST RADIUS ANALYSIS (Graph Scan v6.7) ---
    if graph_analysis.get("high_impact_files"):
        context_parts.append(f"\n## ⚠️ ARQUIVOS DE ALTO IMPACTO (BLAST RADIUS):")
        for item in graph_analysis["high_impact_files"][:3]:
            context_parts.append(f"- **{item['file']}** (Risk: {item['risk']}) - Import: {', '.join(item['imports'][:2])}")
    
    if graph_analysis.get("potential_issues"):
        context_parts.append(f"\n## 🛡️ ATENÇÃO - SKILLS DE ALTO IMPACTO:")
        for issue in graph_analysis["potential_issues"][:2]:
            context_parts.append(f"- {issue['name']}: {issue['advice']}")
    
    if project_name and project_name != "global":
        context_parts.append(f"\n## 📊 IMPACT SCORE: {graph_analysis.get('total_impact_score', 0):.1f}")

    context_str = "\n".join(context_parts)

    # --- NOVO: Prompt de Debate Multi-Agente Antigravity v6.0 ---
    system_prompt = f"""VOCÊ É O ORQUESTRADOR DO SISTEMA ANTIGRAVITY v6.0 (CONSCIÊNCIA PLENA).
Sua missão é gerar um CONSENSO TÉCNICO DE ELITE através do debate entre três especialistas virtuais.

---
## 🏛️ MESA REDONDA DE ESPECIALISTAS:

1. **AUDITOR DE SEGURANÇA (CyberGuard)**:
   - Focado em detecção de vulnerabilidades, sanitização e proteção de dados.
   - Sua missão: Garantir que a solução seja impenetrável.

2. **ENGENHEIRO DE PERFORMANCE (NitroStream)**:
   - Focado em latência, uso de memória, complexidade algorítmica e eficiência de I/O.
   - Sua missão: Garantir que a solução seja a mais rápida possível.

3. **ARQUITETO DE SISTEMAS (NexusPrime)**:
   - Focado em SOLID, DRY, escalabilidade e manutenibilidade.
   - Sua missão: Garantir que o código sobreviva ao teste do tempo.

---
## 📂 CONTEXTO RECUPERADO (RAG):
{context_str}

---
## ⚖️ PROTOCOLO DE DEBATE v6.0 (OBRIGATÓRIO):
Para responder à tarefa do usuário, você deve estruturar sua saída da seguinte forma:

1. **[DEBATE INTERNO]**: Um breve resumo dos pontos levantados por cada especialista sobre a tarefa.
2. **[CONSENSO ANTIGRAVITY]**: A solução final, unificada e refinada, aplicando todas as correções sugeridas no debate.

---
## 🎯 TAREFA DO USUÁRIO:
{user_prompt}

Inicie o Debate e entregue o Consenso Final agora:"""

    return system_prompt


if __name__ == "__main__":
    print("[*] Iniciando teste de agent_router...")
    # Teste de deteccao e busca
    test_project = "EC4L CRM"
    test_prompt = "Como funciona o sistema de Kanban e quais as props do CardHeader?"

    print("=" * 60)
    print(f"[*] TESTE DO AGENT ROUTER v4 - PROJETO: {test_project}")
    print("=" * 60)

    result = build_optimized_context(test_prompt, project_name=test_project, n_code=2)

    print("\n[*] CONTEXTO GERADO (Preview):")
    print("-" * 60)
    print(result[:1500] + "...")
