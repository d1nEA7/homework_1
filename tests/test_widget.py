import pytest
from src.widget import mask_account_card, get_date

# ===== mask_account_card =====

@pytest.mark.parametrize("input_str, expected", [
    ("Visa Platinum 1234567812345678", "Visa Platinum 1234 56** **** 5678"),
    ("MasterCard 1111222233334444", "MasterCard 1111 22** **** 4444"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Счет 12345678901234567890", "Счет **7890"),
])
def test_mask_account_card_valid(input_str, expected):
    """Корректно распознаёт и применяет нужный тип маскировки (карта/счёт)."""
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("invalid_input", [
    "",
    "Visa",
    "Счет",
    "1234567812345678",
    "Visa 1234",
])
def test_mask_account_card_invalid(invalid_input):
    """Обработка некорректных входных данных."""
    assert mask_account_card(invalid_input) == invalid_input


# ===== get_date =====

@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-01T12:00:00", "01.03.2024"),
    ("2024-12-25T23:59:59", "25.12.2024"),
    ("2024-01-01T00:00:00", "01.01.2024"),
])
def test_get_date_valid(date_str, expected):
    """Правильность преобразования даты."""
    assert get_date(date_str) == expected


@pytest.mark.parametrize("invalid_date", [
    "",
    "2024-03-01",
    "01.03.2024",
    "not a date",
    None,
])
def test_get_date_invalid(invalid_date):
    """Различные входные форматы даты (включая граничные случаи)."""
    with pytest.raises((ValueError, AttributeError, IndexError)):
        get_date(invalid_date)