from typing import Iterator
import pytest

def filter_by_currency(transactions:list, currency:str) -> Iterator[dict]:
    """Фильтрует транзакции по заданной валюте."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction

def transaction_descriptions(transactions:list) -> Iterator[str]:
    """Генератор описания каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")

def card_number_generator(num_start:int, num_end:int) -> Iterator[str]:
    """генератор номера карт"""
    for num in range(num_start, num_end + 1):
        card_str = str(num)
        while len(card_str) < 16:
            card_str = "0" + card_str
        result = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        yield result

def test_filter_by_currency_not_found(transactions):
    """тест по несуществующей валюте"""
    result = list(filter_by_currency(transactions, "XXX"))
    assert result == []

def test_transaction_descriptions(transactions):
    """корректные описания для каждой транзакции"""
    result = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]
    assert result == expected

def test_card_number_generator():
    """тест генератора номера карт"""
    result = list(card_number_generator(1, 5))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert result == expected

def test_card_number_generator_format():
    """проверка форматирования"""
    for card in card_number_generator(1, 5):
        parts = card.split()
        assert len(parts) == 4
        for part in parts:
            assert len(part) == 4
            assert part.isdigit()

def test_card_number_generator_min_edge():
    """Минимальное значение"""
    result = list(card_number_generator(1, 1))
    assert result == ["0000 0000 0000 0001"]

def test_card_number_generator_max_edge():
    """максимальное значение"""
    result = list(card_number_generator(9999999999999999, 9999999999999999))
    assert result == ["9999 9999 9999 9999"]

def test_card_number_generator_exhaustion():
    """проверка завершения генерации"""
    gen = card_number_generator(1, 3)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"
    with pytest.raises(StopIteration):
        next(gen)

def test_card_number_generator_empty_range():
    """проверка пустого диапазона"""
    result = list(card_number_generator(10, 5))
    assert result == []

def test_card_number_generator_count():
    """проверка количества элеентов"""
    result = list(card_number_generator(1, 10))
    assert len(result) == 10

@pytest.mark.parametrize("start, end, count", [
    (1, 5, 5),
    (9999999999999990, 9999999999999995, 6),
    (0, 0, 1),
    (100, 200, 101),
])
def test_card_number_generator_count_param(start, end, count):
    assert len(list(card_number_generator(start, end))) == count
    """параметризация для разных диапазонов"""
