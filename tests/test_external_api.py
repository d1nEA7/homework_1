from unittest.mock import patch

import pytest

from src.external_api import convert_currency


def test_convert_currency_rub():
    """Если валюта RUB, возвращаем сумму без конвертации."""
    transaction = {"operationAmount": {"amount": "100.50", "currency": {"code": "RUB"}}}
    result = convert_currency(transaction)
    assert result == 100.50


@patch("src.external_api.os.getenv")
def test_convert_currency_no_api_key(mock_getenv):
    """Если APIKEY нет в .env, выбрасываем ValueError."""
    mock_getenv.return_value = None
    transaction = {"operationAmount": {"amount": "10.0", "currency": {"code": "USD"}}}
    with pytest.raises(ValueError, match="APIKEY не найден в .env"):
        convert_currency(transaction)


@patch("src.external_api.requests.get")
def test_convert_currency_api_error(mock_get):
    """Если API вернул статус не 200, возвращаем 0.0."""
    mock_get.return_value.status_code = 500
    transaction = {"operationAmount": {"amount": "10.0", "currency": {"code": "USD"}}}
    result = convert_currency(transaction)
    assert result == 0.0


@patch("src.external_api.requests.get")
def test_convert_currency_api_success_false(mock_get):
    """Если API вернул success=False, возвращаем 0.0."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"success": False}
    transaction = {"operationAmount": {"amount": "10.0", "currency": {"code": "USD"}}}
    result = convert_currency(transaction)
    assert result == 0.0


@patch("src.external_api.requests.get")
def test_convert_currency_success(mock_get):
    """Если API вернул success=True и result, возвращаем сумму."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"success": True, "result": 900.0}
    transaction = {"operationAmount": {"amount": "10.0", "currency": {"code": "USD"}}}
    result = convert_currency(transaction)
    assert result == 900.0
