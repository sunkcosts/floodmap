from pathlib import Path
from floodmap.env import CACHE


def make_cache():
    if not Path(CACHE).exists():
        Path(CACHE).mkdir()
