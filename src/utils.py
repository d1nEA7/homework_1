import json



def info_transactions() -> list[dict]:
    try:
        with open("data/operation.json") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except FileNotFoundError:
        return []

