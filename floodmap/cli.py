import click


@click.group()
def entry():
    pass


@entry.command()
def configure():
    pass
