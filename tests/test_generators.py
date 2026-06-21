import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def transactions():
    """фикстура с транзакциями"""
    return [
        {
            "id": 1,
            "description": "Перевод организации",
            "operationAmount": {"currency": {"code": "USD"}}
        },
        {
            "id": 2,
            "description": "Перевод со счета на счет",
            "operationAmount": {"currency": {"code": "EUR"}}
        },
        {
            "id": 3,
            "description": "Перевод с карты на карту",
            "operationAmount": {"currency": {"code": "USD"}}
        },
    ]

def test_filter_by_currency_usd(transactions):
    """фильтрация по заданной валюте"""
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    for t in result:
        assert t["operationAmount"]["currency"]["code"] == "USD"



