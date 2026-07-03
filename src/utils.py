import json
from src.external_api import convert_currency


def info_transactions() -> list[dict]:
    """Получает данные о транзакциях из json"""
    try:
        with open("data/operation.json") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except FileNotFoundError:
        return []

transactions = info_transactions()
for transaction in transactions:
def sum_transactions(transaction) -> float:
    """сумма транзакций в рублях"""
    amount = transaction["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if transaction["code"] == "RUB":
        return amount
    else:
        return convert_currency(amount, currency)

