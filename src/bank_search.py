import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция поиска по данным в транзакциях, возвращает список словарей"""
    result = []
    for item in data:
        if re.search(search, item.get('description', ''), re.IGNORECASE):
            result.append(item)
    return result