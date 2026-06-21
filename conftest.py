from typing import Any, Dict, List

import pytest


# Для masks
@pytest.fixture
def card_number() -> str:
    return "1234567812345678"


@pytest.fixture
def account_number() -> str:
    return "73654108430135874305"


# Для processing (список словарей)
@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-02-15T12:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-04-10T09:15:00"},
        {"id": 4, "state": "PENDING", "date": "2024-01-20T08:00:00"},
    ]


# Для widget
@pytest.fixture
def card_string() -> str:
    return "Visa Platinum 1234567812345678"


@pytest.fixture
def account_string() -> str:
    return "Счет 73654108430135874305"


@pytest.fixture
def date_string() -> str:
    return "2024-03-01T12:00:00"
