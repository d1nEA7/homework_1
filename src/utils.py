import json

import src.external_api


def info_transactions(file_path: str) -> list[dict]:
    """Получает данные о транзакциях из json"""  # 1задача
    try:
        with open(file_path) as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def sum_transactions(tr) -> float:
    """сумма транзакций в рублях"""  # 2задача
    amount = float(tr["operationAmount"]["amount"])
    currency = tr["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    else:
        return src.external_api.convert_currency(amount, currency) 


transactions = info_transactions("data/operation.json")
for transaction in transactions:
    rubles = sum_transactions(transaction)
