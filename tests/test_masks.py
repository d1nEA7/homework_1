import pytest

from src.masks import get_mask_account, get_mask_card_number

# ===== get_mask_card_number =====


@pytest.mark.parametrize(
    "card, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("9876543210987654", "9876 54** **** 7654"),
    ],
)
def test_get_mask_card_number_valid(card, expected):
    """Тестирование правильности маскирования номера карты."""
    assert get_mask_card_number(card) == expected


@pytest.mark.parametrize(
    "invalid_card",
    [
        "",  # пустая строка
        "1234",  # слишком короткий
        "123456781234567890",  # слишком длинный
        "1234abcd5678efgh",  # содержит буквы
        12345678,  # не строка
    ],
)
def test_get_mask_card_number_invalid(invalid_card):
    """Граничные случаи и нестандартные длины номеров."""
    with pytest.raises((ValueError, TypeError)):
        get_mask_card_number(invalid_card)


def test_get_mask_card_number_missing():
    """Входная строка, где отсутствует номер карты."""
    with pytest.raises(ValueError):
        get_mask_card_number("")


# ===== get_mask_account =====


@pytest.mark.parametrize(
    "account, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
        ("00000000000000000000", "**0000"),
    ],
)
def test_get_mask_account_valid(account, expected):
    """Тестирование правильности маскирования номера счета."""
    assert get_mask_account(account) == expected


@pytest.mark.parametrize(
    "invalid_account",
    [
        "",  # пустая строка
        "1234",  # слишком короткий
        "123456789012345678901234",  # слишком длинный
        "1234abcd5678efgh5678",  # содержит буквы
        7365410843,  # не строка
    ],
)
def test_get_mask_account_invalid(invalid_account):
    """Различные форматы и длины номеров счетов."""
    with pytest.raises((ValueError, TypeError)):
        get_mask_account(invalid_account)


def test_get_mask_account_too_short():
    """Номер счета меньше ожидаемой длины."""
    with pytest.raises(ValueError):
        get_mask_account("12345")
