import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_currency(transaction: dict) -> float:
    """Принимает транзакцию, конвертирует сумму в рубли."""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    api_key = os.getenv("APIKEY")
    if not api_key:
        raise ValueError("APIKEY не найден в .env")

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"from": currency, "to": "RUB", "amount": amount}
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return 0.0

    data = response.json()
    if data.get("success"):
        return float(data["result"])
    return 0.0
