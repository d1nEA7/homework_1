import json

import src.external_api


def info_transactions(file_path: str) -> list[dict]:
    """Получает данные о транзакциях из json"""
    try:
        with open(file_path) as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def sum_transactions(tr: dict) -> float:
    """сумма транзакций в рублях"""
    return src.external_api.convert_currency(tr)


if __name__ == "__main__":
    transactions = info_transactions("data/operation.json")
    for transaction in transactions:
        rubles = sum_transactions(transaction)
        print(rubles)
