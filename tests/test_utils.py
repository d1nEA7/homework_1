import json
from unittest.mock import mock_open, patch

from src.utils import info_transactions, sum_transactions

# ==================== info_transactions ====================


def test_info_transactions_file_found():
    mock_data = [{"id": 1, "amount": 100}]
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        with patch("json.load", return_value=mock_data):
            result = info_transactions("fake_path.json")
            assert result == mock_data


def test_info_transactions_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = info_transactions("no_file.json")
        assert result == []


def test_info_transactions_not_list():
    mock_data = {"key": "value"}
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        with patch("json.load", return_value=mock_data):
            result = info_transactions("fake.json")
            assert result == []


def test_info_transactions_empty():
    with patch("builtins.open", mock_open(read_data="")):
        with patch("json.load", side_effect=json.JSONDecodeError("", "", 0)):
            result = info_transactions("empty.json")
            assert result == []


# ==================== sum_transactions ====================


def test_sum_transactions_rub():
    transaction = {"operationAmount": {"amount": "100.50", "currency": {"code": "RUB"}}}
    result = sum_transactions(transaction)
    assert result == 100.50


@patch("src.external_api.convert_currency")
def test_sum_transactions_usd(mock_convert):
    transaction = {"operationAmount": {"amount": "50.00", "currency": {"code": "USD"}}}
    mock_convert.return_value = 4500.0
    result = sum_transactions(transaction)
    assert result == 4500.0
    mock_convert.assert_called_once_with(transaction)


@patch("src.external_api.convert_currency")
def test_sum_transactions_eur(mock_convert):
    transaction = {"operationAmount": {"amount": "30.00", "currency": {"code": "EUR"}}}
    mock_convert.return_value = 2700.0
    result = sum_transactions(transaction)
    assert result == 2700.0
    mock_convert.assert_called_once_with(transaction)
