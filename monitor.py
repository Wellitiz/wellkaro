import json
import time
import os
from pathlib import Path
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich import box

console = Console()
LOG_FILE = Path("antigravity_conscience.log")

def get_last_events(n=10):
    if not LOG_FILE.exists():
        return []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        return [json.loads(line) for line in lines[-n:]]

def generate_layout() -> Layout:
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=3)
    )
    layout["body"].split_row(
        Layout(name="left"),
        Layout(name="right", ratio=2)
    )
    return layout

class Monitor:
    def __init__(self):
        self.last_sync = 0
        self.hits = []
        self.expansion = None

    def update(self):
        events = get_last_events(30)
        for event in events:
            if event["timestamp"] > self.last_sync:
                if event["event"] == "query_expansion":
                    self.expansion = event["data"]
                    self.hits = [] # Limpa hits para nova busca
                elif event["event"] == "hit":
                    self.hits.append(event["data"])
                self.last_sync = event["timestamp"]

    def __rich__(self):
        self.update()
        
        # Header
        header = Panel(
            "[bold magenta]🛸 ANTIGRAVITY v5: PAINEL DE CONSCIÊNCIA[/bold magenta]",
            box=box.DOUBLE,
            border_style="magenta"
        )

        # Left Panel: Query Expansion
        expansion_text = "Aguardando busca..."
        if self.expansion:
            expansion_text = f"[bold yellow]Query Original:[/bold yellow]\n{self.expansion['original']}\n\n"
            expansion_text += "[bold cyan]Nuances Geradas:[/bold cyan]\n"
            for var in self.expansion['variations'][1:]:
                expansion_text += f"• {var}\n"
        
        left_panel = Panel(expansion_text, title="🧠 Expansão Semântica", border_style="cyan")

        # Right Panel: Retrieval Hits
        table = Table(expand=True, box=box.SIMPLE)
        table.add_column("Tipo", style="dim")
        table.add_column("Documento", style="bold white")
        table.add_column("Score", justify="right")
        table.add_column("Boosts", justify="center")

        for hit in sorted(self.hits, key=lambda x: x['final_score'], reverse=True)[:15]:
            boosts = []
            if hit.get("project_boost"): boosts.append("🎯")
            if hit.get("solution_boost"): boosts.append("🛠️")
            if hit.get("category_boost"): boosts.append("🏷️")
            
            table.add_row(
                hit["type"],
                hit["name"][:30],
                f"{hit['final_score']:.2f}",
                " ".join(boosts)
            )

        right_panel = Panel(table, title="🔍 Recuperação e Context Boosting", border_style="green")

        # Footer
        footer = Panel(
            "Legenda: 🎯 Projeto Ativo | 🛠️ Solução Documentada | 🏷️ Match de Categoria",
            style="dim white"
        )

        layout = generate_layout()
        layout["header"].update(header)
        layout["left"].update(left_panel)
        layout["right"].update(right_panel)
        layout["footer"].update(footer)
        
        return layout

if __name__ == "__main__":
    monitor = Monitor()
    with Live(monitor, refresh_per_second=4, screen=True) as live:
        try:
            while True:
                time.sleep(0.2)
        except KeyboardInterrupt:
            pass
