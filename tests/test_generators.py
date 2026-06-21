from typing import Any, Dict, Iterator, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    """фикстура с транзакциями"""
    return [
        {"id": 1, "description": "Перевод организации", "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 2, "description": "Перевод со счета на счет", "operationAmount": {"currency": {"code": "EUR"}}},
        {"id": 3, "description": "Перевод с карты на карту", "operationAmount": {"currency": {"code": "USD"}}},
    ]


def test_filter_by_currency_usd(transactions: List[Dict[str, Any]]) -> None:
    """фильтрация по заданной валюте"""
    result: List[Dict[str, Any]] = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    for t in result:
        assert t["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_not_found(transactions: List[Dict[str, Any]]) -> None:
    """тест по несуществующей валюте"""
    result: List[Dict[str, Any]] = list(filter_by_currency(transactions, "XXX"))
    assert result == []


def test_transaction_descriptions(transactions: List[Dict[str, Any]]) -> None:
    """корректные описания для каждой транзакции"""
    result: List[str] = list(transaction_descriptions(transactions))
    expected: List[str] = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]
    assert result == expected


def test_card_number_generator() -> None:
    """тест генератора номера карт"""
    result: List[str] = list(card_number_generator(1, 5))
    expected: List[str] = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert result == expected


def test_card_number_generator_format() -> None:
    """проверка форматирования"""
    for card in card_number_generator(1, 5):
        parts: List[str] = card.split()
        assert len(parts) == 4
        for part in parts:
            assert len(part) == 4
            assert part.isdigit()


def test_card_number_generator_min_edge() -> None:
    """Минимальное значение"""
    result: List[str] = list(card_number_generator(1, 1))
    assert result == ["0000 0000 0000 0001"]


def test_card_number_generator_max_edge() -> None:
    """максимальное значение"""
    result: List[str] = list(card_number_generator(9999999999999999, 9999999999999999))
    assert result == ["9999 9999 9999 9999"]


def test_card_number_generator_exhaustion() -> None:
    """проверка завершения генерации"""
    gen: Iterator[str] = card_number_generator(1, 3)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"
    with pytest.raises(StopIteration):
        next(gen)


def test_card_number_generator_empty_range() -> None:
    """проверка пустого диапазона"""
    result: List[str] = list(card_number_generator(10, 5))
    assert result == []


def test_card_number_generator_count() -> None:
    """проверка количества элементов"""
    result: List[str] = list(card_number_generator(1, 10))
    assert len(result) == 10


@pytest.mark.parametrize(
    "start, end, count",
    [
        (1, 5, 5),
        (9999999999999990, 9999999999999995, 6),
        (0, 0, 1),
        (100, 200, 101),
    ],
)
def test_card_number_generator_count_param(start: int, end: int, count: int) -> None:
    """параметризация для разных диапазонов"""
    assert len(list(card_number_generator(start, end))) == count
