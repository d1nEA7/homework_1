import os
from dotenv import load_dotenv
import requests

load_dotenv()


def convert_currency(amount, currency):
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
        return data["result"]
    return 0.0