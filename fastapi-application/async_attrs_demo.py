import asyncio

from sqlalchemy import select
import typer

from rich import print

from core.models import db_helper, User

app = typer.Typer(
    no_args_is_help=True,
)


async def load_and_show_addresses(
    username: str,
) -> None:
    print(f"[green]Fetching user [bold]{username}[/bold][/green]")

    async with db_helper.session_factory() as session:
        stmt = select(User).where(User.username == username)
        user = await session.scalar(stmt)

        if not user:
            print(f"[red]User [bold]{username}[/bold] not found.[/red]")
            return

        print(f"Fetched user [bold]{user.username}[/bold] (active = {user.is_active})")
        if not user.is_active:
            print(
                f"[red]User [bold]{user.username}[/bold] is inactive, "
                f"skipping addresses loading.[/red]"
            )
            return

        addresses = await user.awaitable_attrs.addresses

        if not addresses:
            print(
                f"[yellow]No addresses for user [bold]{user.username}[/bold][/yellow]"
            )
            return

        print(f"[magenta]Found {len(addresses)} addresses[/magenta]")
        for address in addresses:
            print(f" - {address.city}, [bold]{address.street}[/bold]")


@app.command()
def demo(username: str) -> None:
    print(f"[blue]Demo Async Attrs for [bold]{username}[/bold][/blue]")
    asyncio.run(load_and_show_addresses(username))


if __name__ == "__main__":
    app()
