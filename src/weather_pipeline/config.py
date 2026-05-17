import json
from pathlib import Path

def load_cities(config_path: str | Path) -> list[dict]:
    path = Path(config_path)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)