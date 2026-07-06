from unittest.mock import patch

from src.external_api import convert_currency


@patch("src.external_api.requests.get")
def test_fuo(mock_get):
    """Тест конвертации валюты."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"success": True, "result": 900.0}

    transaction = {"operationAmount": {"amount": "10.0", "currency": {"code": "USD"}}}
    result = convert_currency(transaction)

    assert result == 900.0
