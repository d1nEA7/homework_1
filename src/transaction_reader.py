from pathlib import Path

import pandas as pd


def read_transactions_csv(path: str = "src/transactions.csv") -> list[dict]:
    """Функция чтения CSV файла транзакций."""
    if not Path(path).exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    df = pd.read_csv(path, sep=";")  # ← добавлен sep=';'
    return df.to_dict(orient="records")


def read_transactions_excel(path: str = "src/transactions_excel.xlsx") -> list[dict]:
    """Функция чтения Excel файла транзакций."""
    if not Path(path).exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    df = pd.read_excel(path)
    return df.to_dict(orient="records")


if __name__ == "__main__":
    data = read_transactions_excel("src/transactions_excel.xlsx")
    print(data)
