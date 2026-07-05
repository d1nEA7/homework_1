import pytest
from unittest.mock import patch
from src.external_api import convert_currency


# ===== Тест 1: валюта RUB =====

def test_convert_currency_rub():
    """Если валюта RUB, возвращаем сумму без конвертации."""
    result = convert_currency(100.50, "RUB")
    assert result == 100.50


# ===== Тест 2: ошибка — нет APIKEY =====

@patch("src.external_api.os.getenv")
def test_convert_currency_no_api_key(mock_getenv):
    """Если APIKEY нет в .env, выбрасываем ValueError."""
    mock_getenv.return_value = None
    with pytest.raises(ValueError, match="APIKEY не найден в .env"):
        convert_currency(10.0, "USD")


# ===== Тест 3: API вернул ошибку (статус не 200) =====

@patch("src.external_api.requests.get")
def test_convert_currency_api_error(mock_get):
    """Если API вернул статус не 200, возвращаем 0.0."""
    mock_get.return_value.status_code = 500
    result = convert_currency(10.0, "USD")
    assert result == 0.0


# ===== Тест 4: API вернул success=False =====

@patch("src.external_api.requests.get")
def test_convert_currency_api_success_false(mock_get):
    """Если API вернул success=False, возвращаем 0.0."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"success": False}
    result = convert_currency(10.0, "USD")
    assert result == 0.0


# ===== Тест 5: успешная конвертация =====

@patch("src.external_api.requests.get")
def test_convert_currency_success(mock_get):
    """Если API вернул success=True и result, возвращаем сумму."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"success": True, "result": 900.0}
    result = convert_currency(10.0, "USD")
    assert result == 900.0