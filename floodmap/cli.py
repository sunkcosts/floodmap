import click
from floodmap.term import vprint


@click.group()
def entry():
    pass


@entry.command()
def configure():
    vprint("[green]Please enter your mapbox API token below.[\green]")
