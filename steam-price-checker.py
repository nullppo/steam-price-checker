import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
from rich.align import Align
from rich.spinner import Spinner
from rich.live import Live
from rich import box


console = Console()

STEAM_BLUE = "bold cyan"
ACCENT = "bold green"
ERROR = "bold red"
WARN = "bold yellow"
DIM = "dim white"


def print_banner():
    banner = Text()
    banner.append("STEAM-", style="bold cyan")
    banner.append("PRICE-", style="bold white")
    banner.append("CHECKER-", style="bold green")

    console.print()
    console.print(Panel(
        Align.center(banner),
        subtitle="[dim]powered by CheapShark & Steam API[/dim]",
        border_style="cyan",
        padding=(0, 4),
    ))
    console.print()


def print_menu():
    table = Table(
        box=box.ROUNDED,
        border_style="cyan",
        show_header=False,
        padding=(0, 2),
        expand=False,
    )
    table.add_column("Key", style="bold cyan", width=4)
    table.add_column("Option", style="white")

    table.add_row("1", "🔍  Search game price by name")
    table.add_row("2", "🌍  Compare prices across countries")
    table.add_row("3", "💸  Find lowest price by game name")
    table.add_row("0", "🚪  Exit")

    console.print(Align.center(table))
    console.print()


def spinner(url, params, label="Fetching data..."):
    result = {}
    with Live(
        Spinner("dots", text=f"[cyan]{label}[/cyan]"),
        console=console,
        refresh_per_second=10,
        transient=True,
    ):
        try:
            r = requests.get(url, params=params, timeout=10)
            result["response"] = r
        except requests.exceptions.RequestException as e:
            result["error"] = str(e)
    return result


def search_game():
    console.print(Panel("[bold cyan]Search Game[/bold cyan]", border_style="cyan"))

    game_name = Prompt.ask("[cyan]Game name[/cyan]").strip()
    country = Prompt.ask(
        "[cyan]Country code[/cyan] [dim](ru / ua / kz / tr / ar / us ...)[/dim]",
        default="us"
    ).strip().lower()

    res = spinner(
        "https://www.cheapshark.com/api/1.0/games",
        {"title": game_name, "limit": 5},
        label="Searching...",
    )

    if "error" in res:
        console.print(f"[{ERROR}]Network error:[/{ERROR}] {res['error']}")
        return

    r = res["response"]
    if r.status_code != 200:
        console.print(f"[{ERROR}]CheapShark API error:[/{ERROR}] HTTP {r.status_code}")
        return

    data = r.json()[:1]
    if not data:
        console.print(f"[{WARN}]No game found for '[bold]{game_name}[/bold]'[/{WARN}]")
        return

    for game in data:
        steamid = game.get("steamAppID")
        if not steamid:
            console.print(f"[{WARN}]No Steam ID for this game.[/{WARN}]")
            continue

        res2 = spinner(
            "https://store.steampowered.com/api/appdetails",
            {"appids": steamid, "cc": country},
            label=f"Fetching Steam data for region [bold]{country.upper()}[/bold]...",
        )

        if "error" in res2:
            console.print(f"[{ERROR}]Steam network error:[/{ERROR}] {res2['error']}")
            continue

        r2 = res2["response"]
        if r2.status_code != 200:
            console.print(f"[{ERROR}]Steam API error:[/{ERROR}] HTTP {r2.status_code}")
            continue

        gameinfo = r2.json().get(str(steamid))
        if not gameinfo or not gameinfo.get("success"):
            console.print(f"[{WARN}]Steam returned no data (region may be unsupported).[/{WARN}]")
            continue

        game_data = gameinfo["data"]
        name = game_data.get("name", "Unknown")
        price = game_data.get("price_overview")

        if price:
            discount = price["discount_percent"]
            final = price["final_formatted"]
            initial = price["initial_formatted"]

            result_table = Table(
                box=box.ROUNDED,
                border_style="green",
                show_header=False,
                padding=(0, 2),
            )
            result_table.add_column("Field", style="dim white", width=18)
            result_table.add_column("Value", style="bold white")

            result_table.add_row("Game", f"[bold cyan]{name}[/bold cyan]")
            result_table.add_row("Country", f"[bold]{country.upper()}[/bold]")
            result_table.add_row("Current price", f"[bold green]{final}[/bold green]")
            result_table.add_row("Base price", f"[dim]{initial}[/dim]")

            if discount > 0:
                result_table.add_row(
                    "🔥 Discount",
                    f"[bold red]-{discount}%[/bold red]"
                )
            else:
                result_table.add_row("🔥 Discount", "[dim]No discount[/dim]")

            console.print()
            console.print(Panel(
                result_table,
                title="[bold green]✅ Game Found[/bold green]",
                border_style="green",
            ))
        else:
            console.print(Panel(
                f"[{WARN}]«{name}» is either [bold]free[/bold] or [bold]unavailable[/bold] in region '[bold]{country.upper()}[/bold]'.[/{WARN}]",
                border_style="yellow",
            ))


def main():
    print_banner()

    while True:
        print_menu()
        ch = Prompt.ask("[bold cyan]Choose option[/bold cyan]", choices=["0", "1", "2", "3"], show_choices=False).strip()

        console.print()

        try:
            match ch:
                case "1":
                    search_game()
                case "2":
                    console.print(Panel("[yellow]In development...[/yellow]", border_style="yellow"))
                case "3":
                    console.print(Panel("[yellow]In development...[/yellow]", border_style="yellow"))
                case "0":
                    console.print(Panel("[bold cyan]👋 Bye! See you next time.[/bold cyan]", border_style="cyan"))
                    break

        except KeyboardInterrupt:
            console.print()
            console.print(Panel("[bold cyan]Bye![/bold cyan]", border_style="cyan"))
            break

        console.print()


if __name__ == "__main__":
    main()