import os
from dotenv import load_dotenv
load_dotenv()
import requests

from utils import transaction

api_key = os.getenv("APIKEY")


def convert_currency():
    """функция конвертации валюты"""
    response = requests.get(url, headers=headers, params=transaction)
    status_code = response.status_code
    result = response.json()
    return result