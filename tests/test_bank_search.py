import pytest

from src.bank_search import process_bank_operations, process_bank_search


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми транзакциями."""
    return [
        {"description": "Перевод организации"},
        {"description": "Покупка в магазине"},
        {"description": "Перевод на карту"},
        {"description": "Оплата услуг"},
    ]


# ==================== Тесты для process_bank_search ====================


def test_process_bank_search_found(sample_transactions):
    """Проверяет, что поиск находит транзакции с нужным словом."""
    result = process_bank_search(sample_transactions, "перевод")
    assert len(result) == 2
    assert all("Перевод" in item["description"] for item in result)


def test_process_bank_search_not_found(sample_transactions):
    """Проверяет, что при отсутствии слова возвращается пустой список."""
    result = process_bank_search(sample_transactions, "кредит")
    assert result == []


def test_process_bank_search_case_insensitive(sample_transactions):
    """Проверяет, что поиск игнорирует регистр."""
    result = process_bank_search(sample_transactions, "ПЕРЕВОД")
    assert len(result) == 2


def test_process_bank_search_empty_description():
    """Проверяет, что пустое описание не вызывает ошибку."""
    data = [{"description": ""}, {"description": "Перевод"}]
    result = process_bank_search(data, "перевод")
    assert len(result) == 1


def test_process_bank_search_no_description():
    """Проверяет, что отсутствие ключа description не вызывает ошибку."""
    data = [{"id": 1}, {"description": "Перевод"}]
    result = process_bank_search(data, "перевод")
    assert len(result) == 1


# ==================== Тесты для process_bank_operations ====================


def test_process_bank_operations_counting():
    """Проверяет, что функция правильно подсчитывает операции по категориям."""
    data = [
        {"description": "Перевод организации"},
        {"description": "Покупка в магазине"},
        {"description": "Перевод на карту"},
        {"description": "Оплата услуг"},
    ]
    categories = ["Перевод", "Покупка", "Оплата"]
    result = process_bank_operations(data, categories)
    expected = {"Перевод": 2, "Покупка": 1, "Оплата": 1}
    assert result == expected


def test_process_bank_operations_empty():
    """Проверяет, что при пустом списке транзакций возвращаются нули."""
    data = []
    categories = ["Перевод", "Покупка"]
    result = process_bank_operations(data, categories)
    assert result == {"Перевод": 0, "Покупка": 0}


def test_process_bank_operations_no_description():
    """Проверяет, что отсутствие description не вызывает ошибку."""
    data = [{"id": 1}, {"description": "Перевод"}]
    categories = ["Перевод"]
    result = process_bank_operations(data, categories)
    assert result == {"Перевод": 1}


def test_process_bank_operations_case_insensitive():
    """Проверяет, что подсчёт игнорирует регистр."""
    data = [{"description": "перевод организации"}]
    categories = ["Перевод"]
    result = process_bank_operations(data, categories)
    assert result == {"Перевод": 1}
