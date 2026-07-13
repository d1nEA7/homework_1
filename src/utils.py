import json
import logging

import src.external_api

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logs/masks.log",
    filemode="w",
)

info_transactions_logger = logging.getLogger("info_transactions_logger")
sum_transactions_logger = logging.getLogger("sum_transactions_logger")


def info_transactions(file_path: str) -> list[dict]:
    """Получает данные о транзакциях из json"""
    info_transactions_logger.info("запуск info_transactions")
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
            info_transactions_logger.info("Получает дынные из json")
            if isinstance(data, list):
                info_transactions_logger.info("тип данных list")
                return data
            info_transactions_logger.info("вернула список")
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        info_transactions_logger.error("ошибка при чтении json")
        return []


def sum_transactions(tr: dict) -> float:
    """конвертирует в руб., считает сумму транзакций в рублях"""
    sum_transactions_logger.info("запуск sum_transactions")
    return src.external_api.convert_currency(tr)


if __name__ == "__main__":
    transactions = info_transactions("data/operations.json")
    for transaction in transactions:
        rubles = sum_transactions(transaction)
        print(rubles)
