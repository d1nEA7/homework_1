from src.bank_search import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.transaction_reader import read_transactions_csv, read_transactions_excel
from src.utils import info_transactions
from src.widget import get_date, mask_account_card


def main() -> None:
    transactions = []
    selected = False

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while not selected:
        user = input(
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
            "Ваш выбор: "
        )

        if user == "1":
            print("Для обработки выбран JSON-файл.")
            transactions = info_transactions("data/operations.json")
            selected = True
        elif user == "2":
            print("Для обработки выбран CSV-файл.")
            transactions = read_transactions_csv("src/transactions.csv")
            selected = True
        elif user == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions = read_transactions_excel("src/transactions_excel.xlsx")
            selected = True
        else:
            print("Неверный выбор. Попробуйте снова.\n")

    status = ""
    while status not in ["EXECUTED", "CANCELED", "PENDING"]:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            "Ваш выбор: "
        ).upper()
        if status not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {status} недоступен. Попробуйте снова.\n")

    print(f"Операции отфильтрованы по статусу {status}")

    if status == "EXECUTED":
        transactions = filter_by_state(transactions, "EXECUTED")
    elif status == "CANCELED":
        transactions = filter_by_state(transactions, "CANCELED")
    elif status == "PENDING":
        transactions = filter_by_state(transactions, "PENDING")

    sorted_by_date = input("Отсортировать операции по дате? Да/Нет").lower()
    if sorted_by_date == "да":
        sort_reverse = input("Отсортировать по возрастанию или по убыванию?").lower()
        if sort_reverse == "по возрастанию":
            transactions = sort_by_date(transactions, reverse=False)
        elif sort_reverse == "по убыванию":
            transactions = sort_by_date(transactions, reverse=True)
    filter_rub = input("Выводить только рублевые транзакции? Да/Нет").lower()
    if filter_rub == "да":
        rub_transactions = []
        for transaction in transactions:
            currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
            if currency == "RUB":
                rub_transactions.append(transaction)
        transactions = rub_transactions

    filter_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
    if filter_by_word == "да":
        search_word = input("Введите слово для поиска: ")
        transactions = process_bank_search(transactions, search_word)

    print("Распечатываю итоговый список транзакций...")
    if transactions:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            display_transaction(transaction)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def display_transaction(transaction: dict) -> None:
    """Форматирует транзакцию"""
    format_date = get_date(transaction["date"])
    description = transaction.get("description", "Описание отсутствует")
    from_account = mask_account_card(transaction.get("from", ""))
    to_account = mask_account_card(transaction.get("to", ""))
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    if from_account and to_account:
        transfer_str = f"{from_account} -> {to_account}"
    elif to_account:
        transfer_str = to_account
    elif from_account:
        transfer_str = from_account
    else:
        transfer_str = ""

    print(f"{format_date} {description}")
    if transfer_str:
        print(transfer_str)
    print(f"Сумма: {amount} {currency}")
    print()


if __name__ == "__main__":
    main()
