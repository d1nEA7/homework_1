import requests

from utils import transaction




def convert_valute():
    """функция"""
    response = requests.get(url, headers=headers, params=transaction)
    status_code = response.status_code
    result = response.json()