from typing import Iterator

def filter_by_currency(transactions:list, currency:str) -> Iterator[dict]:
    """Фильтрует транзакции по заданной валюте."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction

def transaction_descriptions(transactions:list) -> Iterator[str]:
    """Генератор описания каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")
