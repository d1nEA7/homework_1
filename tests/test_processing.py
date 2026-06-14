import pytest

from src.processing import filter_by_state, sort_by_date


# Фикстура с данными
@pytest.fixture
def transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-02-15T12:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-04-10T09:15:00"},
        {"id": 4, "state": "PENDING", "date": "2024-01-20T08:00:00"},
    ]


# ===== filter_by_state =====


def test_filter_by_state_default(transactions):
    """Фильтрация по умолчанию (state='EXECUTED')."""
    filtered = filter_by_state(transactions)
    assert len(filtered) == 2
    for item in filtered:
        assert item["state"] == "EXECUTED"


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 1),
        ("PENDING", 1),
        ("NONEXISTENT", 0),
    ],
)
def test_filter_by_state_param(transactions, state, expected_count):
    """Параметризация для различных возможных значений статуса state."""
    filtered = filter_by_state(transactions, state)
    assert len(filtered) == expected_count


# ===== sort_by_date =====


def test_sort_by_date_descending(transactions):
    """Сортировка по дате в порядке убывания."""
    sorted_list = sort_by_date(transactions)
    dates = [item["date"] for item in sorted_list]
    assert dates == [
        "2024-04-10T09:15:00",
        "2024-03-01T10:00:00",
        "2024-02-15T12:30:00",
        "2024-01-20T08:00:00",
    ]


def test_sort_by_date_ascending(transactions):
    """Сортировка по дате в порядке возрастания."""
    sorted_list = sort_by_date(transactions, reverse=False)
    dates = [item["date"] for item in sorted_list]
    assert dates == [
        "2024-01-20T08:00:00",
        "2024-02-15T12:30:00",
        "2024-03-01T10:00:00",
        "2024-04-10T09:15:00",
    ]


def test_sort_by_date_same_dates():
    """Корректность сортировки при одинаковых датах."""
    same = [
        {"id": 1, "date": "2024-01-01"},
        {"id": 2, "date": "2024-01-01"},
    ]
    sorted_list = sort_by_date(same)
    assert len(sorted_list) == 2
    assert sorted_list[0]["date"] == sorted_list[1]["date"]


@pytest.mark.parametrize(
    "bad_dates",
    [
        [{"id": 1, "date": None}],
        [{"id": 1, "date": ""}],
        [{"id": 1, "date": "not a date"}],
    ],
)
def test_sort_by_date_invalid(bad_dates):
    """Некорректные или нестандартные форматы дат."""
    with pytest.raises((ValueError, TypeError, AttributeError)):
        sort_by_date(bad_dates)
