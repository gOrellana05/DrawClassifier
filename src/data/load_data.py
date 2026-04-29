from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parents[2]


def load_ndjson(filename, max_samples=2000):
    file_path = BASE_DIR / "data" / "raw" / filename

    data = []

    with open(file_path, "r") as f:
        for i, line in enumerate(f):
            if i >= max_samples:
                break
            data.append(json.loads(line))

    return data