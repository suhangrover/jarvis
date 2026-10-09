from rich.console import Console
from rich.panel import Panel

from tools.system import system_info

console = Console()


def main():
    console.print(
        Panel(
            "[bold cyan]Jarvis[/bold cyan]\n"
            "Juixce",
            title="System Inspection",
            border_style="cyan",
        )
    )
    info = system_info()

    for key, value in info.items():
        label = key.replace("_", " ").title()
        console.print(f"[cyan]{label}:[/cyan] {value}") #it uses rich's markup
main()