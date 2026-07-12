from unittest.mock import patch

import pandas as pd
import pytest

from src.transaction_reader import read_transactions_csv, read_transactions_excel


@pytest.fixture
def sample_transactions():
    """фикстура для теста входных данных о транзакциях"""
    return [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
    ]


@patch("pandas.read_csv")
@patch("pathlib.Path.exists")
def test_read_transactions_csv(mock_exists, mock_read_csv, sample_transactions):
    """проверка мок и патч на работу чтения csv файла"""
    mock_exists.return_value = True  # файл существует
    mock_df = pd.DataFrame(sample_transactions)
    mock_read_csv.return_value = mock_df
    result = read_transactions_csv("fake.csv")
    assert result == sample_transactions
    mock_read_csv.assert_called_once_with("fake.csv", sep=";")


@patch("pandas.read_excel")
@patch("pathlib.Path.exists")
def test_read_transactions_excel(mock_exists, mock_read_excel, sample_transactions):
    """Тест чтения Excel-файла с транзакциями"""
    mock_df = pd.DataFrame(sample_transactions)  # ← создаём DataFrame из фикстуры
    mock_read_excel.return_value = mock_df
    result = read_transactions_excel("fake.xlsx")
    mock_exists.return_value = True
    assert result == sample_transactions
    mock_read_excel.assert_called_once_with("fake.xlsx")
