import os
import click
import subprocess
import requests
from pick import pick
from pathlib import Path
from floodmap.cache import make_cache
from floodmap.term import vprint, clear
from floodmap.env import TOKEN, ENDPOINT


@click.group()
def entry():
    pass


@entry.group()
def token():
    pass


@token.command()
def save():
    clear()
    make_cache()
    vprint("[blue]Mapbox API Token[/blue]")
    api_token = str(input("❯ "))
    resp = requests.get(ENDPOINT.tokens(api_token))
    code = resp.json()["code"]
    if code == "TokenValid":
        if Path(TOKEN).exists():
            selection = pick(options=["Yes", "No"], title="Overwrite Existing")
            if selection[0] == "No":
                vprint("[yellow]Exit: No Overwrite[/yellow]")
                exit()
        with open(TOKEN, "w") as token:
            token.write(api_token)
        token.close()
        vprint("[green]Token Saved[/green]")
    elif code == "TokenMalformed":
        vprint("[red]API Token Invalid[/red]")
        exit()
    else:
        vprint("[red]Unidentified Error[/red]")
        exit()


@token.command()
def view():
    if Path(TOKEN).exists():
        with open(TOKEN, "r") as token:
            api_token = token.read().split("\n")[0]
            vprint(f"[blue]{api_token}[/blue]")
    else:
        vprint(f"[yellow]No Token Available[/yellow]")


@token.command()
def copy():
    if Path(TOKEN).exists():
        with open(TOKEN, "r") as token:
            api_token = token.read().split("\n")[0]
        token.close()
        subprocess.run("pbcopy", text=True, input=api_token)
        vprint(f"[green]Token Copied[/green]")
    else:
        vprint(f"[yellow]No Token Available[/yellow]")


@token.command()
def delete():
    if Path(TOKEN).exists():
        os.remove(TOKEN)
        vprint("[green]Token Deleted[/green]")
    else:
        vprint(f"[yellow]No Token Available[/yellow]")
