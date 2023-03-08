import click
import requests
from floodmap.cache import make_cache
from floodmap.term import vprint, clear
from floodmap.env import CACHE, ENDPOINT


@click.group()
def entry():
    pass


@entry.command()
def configure():
    make_cache()
    clear()
    vprint("[blue]Mapbox API Key[/blue]")
    api_token = str(input("❯ "))
    resp = requests.get(ENDPOINT.tokens(api_token))
    code = resp.json()["code"]
    if code == "TokenValid":
        with open(f"{CACHE}/mapbox", "w") as token:
            token.write(api_token)
        token.close()
        vprint("[green]Token saved to local cache[\green]")
    elif code == "TokenMalformed":
        vprint("[red]API Key Invalid[/red]")
        exit()
    else:
        vprint("[red]Unidentified Error[/red]")
        exit()
