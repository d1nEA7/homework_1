from unittest.mock import patch

from src.external_api import convert_currency


@patch("src.external_api.os.getenv")
@patch("src.external_api.requests.get")
def test_convert_currency_api_error(mock_get, mock_getenv):
    mock_getenv.return_value = "fake_key"
    mock_get.return_value.status_code = 500
    transaction = {"operationAmount": {"amount": "10.0", "currency": {"code": "USD"}}}
    result = convert_currency(transaction)
    assert result == 0.0


@patch("src.external_api.os.getenv")
@patch("src.external_api.requests.get")
def test_convert_currency_api_success_false(mock_get, mock_getenv):
    mock_getenv.return_value = "fake_key"
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"success": False}
    transaction = {"operationAmount": {"amount": "10.0", "currency": {"code": "USD"}}}
    result = convert_currency(transaction)
    assert result == 0.0


@patch("src.external_api.os.getenv")
@patch("src.external_api.requests.get")
def test_convert_currency_success(mock_get, mock_getenv):
    mock_getenv.return_value = "fake_key"
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"success": True, "result": 900.0}
    transaction = {"operationAmount": {"amount": "10.0", "currency": {"code": "USD"}}}
    result = convert_currency(transaction)
    assert result == 900.0


@patch("src.external_api.os.getenv")
@patch("src.external_api.requests.get")
def test_fuo(mock_get, mock_getenv):
    mock_getenv.return_value = "fake_key"
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"success": True, "result": 900.0}
    transaction = {"operationAmount": {"amount": "10.0", "currency": {"code": "USD"}}}
    result = convert_currency(transaction)
    assert result == 900.0
