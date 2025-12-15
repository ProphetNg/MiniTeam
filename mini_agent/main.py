import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from team import Manager

app = typer.Typer()
console = Console()

@app.command()
def main():
    """
    MiniTeam CLI - AI Development Squad
    """
    console.print(Panel.fit(
        "[bold blue]Welcome to MiniTeam via CLI[/bold blue]\n"
        "[dim]Your AI Development Squad is ready.[/dim]\n"
        "Roles: [green]Manager[/green], [cyan]Frontend[/cyan], [yellow]Backend[/yellow], [magenta]QA[/magenta], [white]Docs[/white]",
        title="🤖 MiniTeam"
    ))
    
    try:
        agent = Manager()
        console.print("[dim]Manager initialized.[/dim]")
    except Exception as e:
        console.print(f"[bold red]Failed to init Manager: {e}[/bold red]")
        return
    
    while True:
        try:
            user_input = Prompt.ask("\n[bold green]You[/bold green]")
            
            if user_input.lower() in ['exit', 'quit']:
                console.print("Goodbye!", style="green")
                break
                
            if not user_input.strip():
                continue
                
            with console.status("[bold green]Manager is thinking & delegating...[/bold green]", spinner="dots"):
                response = agent.chat(user_input)
            
            console.print(Panel(Markdown(response), title="[bold blue]Manager[/bold blue]", border_style="blue"))
            
        except KeyboardInterrupt:
            console.print("\nExiting...", style="yellow")
            break
        except Exception as e:
            console.print(f"An error occurred: {str(e)}", style="bold red")

if __name__ == "__main__":
    app()
