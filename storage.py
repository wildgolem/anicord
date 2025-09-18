import json
import os

def load_ids():
    if not os.path.exists("data.json"):
        return set()
    try:
        with open("data.json", "r") as f:
            return set(json.load(f))
    except (json.JSONDecodeError, FileNotFoundError):
        return set()

def save_ids(ids):
    with open("data.json", "w") as f:
        json.dump(list(ids), f, indent=2)
