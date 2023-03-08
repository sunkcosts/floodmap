import click
from floodmap.term import vprint, clear


@click.group()
def entry():
    pass


@entry.command()
def configure():
    clear()
    vprint("[green]Mapbox API Key[/green]")
    api_token = str(input("❯ "))
