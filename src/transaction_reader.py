import pandas as pd



def read_transactions_csv(path: str = "src/transactions.csv") -> list[dict]:
    """Функция чтения CSV файла транзакций."""
    df = pd.read_csv(path)
    return df.to_dict(orient='records')


def read_transactions_excel(path: str = "src/transactions_excel.xlsx") -> list[dict]:
    """Функция чтения Excel файла транзакций."""
    df = pd.read_excel(path)
    return df.to_dict(orient='records')