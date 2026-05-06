import os
import subprocess

repos = [
    "1NickPappas/move-code-quality-skill",
    "8144225309/superscalar-mcp",
    "AlmogBaku/debug-skill",
    "AlterLab-IEU/AlterLab-Academic-Skills",
    "AlterLab-IEU/AlterLab-FC-Skills",
    "AlterLab-IEU/AlterLab_GameForge",
    "Ashutos1997/claude-design-auditor-skill",
    "BehiSecc/VibeSec-Skill",
    "ChainAware/behavioral-prediction-mcp",
    "ComposioHQ/awesome-claude-skills",
    "Digidai/product-manager-skills",
    "EmblemCompany/Agent-skills",
    "HeshamFS/materials-simulation-skills",
    "K-Dense-AI/claude-scientific-skills",
    "Linked-API/linkedin-skills",
    "NoizAI/skills",
    "Octav-Labs/octav-api-skill",
    "RioTheGreat-ai/agentfund-mcp",
    "SeifBenayed/claude-code-sdk",
    "Square-Zero-Labs/video-prompting-skill",
    "Swiftner/Factory-Floor",
    "TheQmaks/crowdcast",
    "TomGranot/hubspot-admin-skills",
    "Valian/linear-cli-skill",
    "Xquik-dev/x-twitter-scraper",
    "adiny/moodtrip-hotel-search",
    "agamm/claude-code-owasp",
    "agent-cards/skill",
    "agentbay-ai/agentbay-skills",
    "anthropics/skills",
    "avifenesh/agnix",
    "backnotprop/plannotator",
    "bitwize-music-studio/claude-ai-music-skills",
    "bluzername/claude-code-terminal-title",
    "coffeefuelbump/csv-data-summarizer-claude-skill",
    "coinpaprika/skills",
    "conorbronsdon/avoid-ai-writing",
    "daxaur/openpaw",
    "deanpeters/Product-Manager-Skills",
    "deapi-ai/claude-code-skills",
    "digitalsamba/claude-code-video-toolkit",
    "emaynard/claude-family-history-research-skill",
    "framix-team/skill-email-html-mjml",
    "glacierphonk/naming",
    "glitternetwork/skills",
    "guia-matthieu/clawfu-skills",
    "hashicorp/agent-skills",
    "huifer/Claude-Ally-Health",
    "ivan-magda/claude-code-plugin-template",
    "jacob-g-park/polaris-datainsight-doc-extract",
    "jahro-console/unity-agent-skills",
    "jeffallan/claude-skills",
    "jonathimer/devmarketing-skills",
    "jthack/ffuf_claude_skill",
    "krodak/clickup-cli",
    "mattjoyce/kanban-skill",
    "mhattingpete/claude-skills-marketplace",
    "michalparkola/tapestry-skills-for-claude-code",
    "obra/superpowers",
    "oil-oil/oiloil-ui-ux-guide",
    "olgasafonova/SkillCheck-Free",
    "omkamal/pypict-claude-skill",
    "openclaw/skills",
    "pjt222/agent-almanac",
    "polaroteam/moltdj-skill",
    "product-on-purpose/pm-skills",
    "raintree-technology/claude-starter",
    "rebelytics/one-skill-to-rule-them-all",
    "ryanbbrown/revealjs-skill",
    "sanjay3290/ai-skills",
    "shepsci/kaggle-skill",
    "shmlkv/dna-claude-analysis",
    "smerchek/claude-epub-skill",
    "spartan-stratos/spartan-ai-toolkit",
    "takechanman1228/claude-ecom",
    "tasteray/skills",
    "testdino-hq/playwright-skill",
    "trailofbits/skills",
    "uriva/find-scene-skill",
    "video-db/skills",
    "wannabehero/charles-proxy-extract-skill",
    "wd041216-bit/ironclaw-agent-guard",
    "wondelai/skills",
    "wrsmith108/linear-claude-skill",
    "wrsmith108/varlock-claude-skill",
    "ykdojo/claude-code-tips",
    "ykdojo/gh-star-history",
    "ykdojo/paper-search",
    "zagmoai/public-google-drive",
    "zxkane/aws-skills"
]

base_path = r"c:\Users\welli\Downloads\Antigravity\.agent\specialists\bulk_import"
os.makedirs(base_path, exist_ok=True)

for repo in repos:
    user, name = repo.split('/')
    target_dir = os.path.join(base_path, f"{user}_{name}")
    if os.path.exists(target_dir):
        print(f"[*] Skipping {repo} (already exists)")
        continue
    
    print(f"[*] Cloning {repo}...")
    try:
        subprocess.run(["git", "clone", "--depth", "1", f"https://github.com/{repo}", target_dir], check=True)
    except Exception as e:
        print(f"[!] Failed to clone {repo}: {e}")
