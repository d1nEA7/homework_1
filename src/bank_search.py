import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция поиска по данным в транзакциях, возвращает список словарей"""
    result = []
    for item in data:
        if re.search(search, item.get("description", ""), re.IGNORECASE):
            result.append(item)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    descriptions = [operation["description"] for operation in data]
    count = Counter(descriptions)
    result = {category: count[category] for category in categories}
    return result
