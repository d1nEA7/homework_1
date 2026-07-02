import json



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
    if transaction["code"] == "RUB":
        return amount
    else:
        