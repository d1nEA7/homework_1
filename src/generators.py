from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator[dict]:
    """Фильтрует транзакции по заданной валюте."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Iterator[str]:
    """Генератор описания каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(num_start: int, num_end: int) -> Iterator[str]:
    """генератор номера карт"""
    for num in range(num_start, num_end + 1):
        card_str = str(num)
        while len(card_str) < 16:
            card_str = "0" + card_str
        result = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        yield result
