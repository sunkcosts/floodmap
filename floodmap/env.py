from pathlib import Path
from pydantic import BaseModel

# Local
HOME = Path.home()
CACHE = HOME / ".floodmap"

# Web
class Endpoint(BaseModel):
    base: str = "https://api.mapbox.com"

    def tokens(self, key: str) -> str:
        return f"{self.base}/tokens/v2?access_token={key}"
