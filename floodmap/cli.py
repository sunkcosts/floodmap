import click
from floodmap.term import vprint, clear


@click.group()
def entry():
    pass


@entry.command()
def configure():
    clear()
    vprint("[green]Please enter your mapbox API token below.[/green]")
    api_token = str(input("❯"))
