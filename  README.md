#Домашняя работа по теме "обработка банковских операций"

##Описание:

Этот проект был создан с целью получений знаний и практики, оттачивания навыков программирования при изучении курсов от онлайн школы программирования "SkyPro"
Разработка делалась в приложении "Pycharm"

##Описание функций в проекте: 

В данной домашней работе содержатся функции для маскировки банковских карт, которые написаны в модуле mask.py
А так же есть функции по сортировке списков по дате и возвращает новый список словарей по значению EXECUTED
Ещё есть файлы gitignor, flake8 в которых находятся параметры работы, так же есть функции декораторы, и тесты для них.
Есть функции для чтения данных о транзакциях из csv и excel файлов.

1. Клонируйте репозиторий:
```
git clone git@github.com:d1nEA7/homework_1.git
```
2. Установите зависимости:
```
poetry install
```
3. Запуск программы (на OS WINDOWS):
```
python -m src.main
```
## ⚙️ Список функций

### Модуль `utils.py`
- `info_transactions(file_path: str) -> list[dict]` — читает JSON-файл и возвращает список транзакций
- `sum_transactions(tr: dict) -> float` — конвертирует сумму транзакции в рубли (использует `convert_currency`)

### Модуль `transaction_reader.py`
- `read_transactions_csv(path: str) -> list[dict]` — читает CSV-файл с транзакциями (разделитель `;`)
- `read_transactions_excel(path: str) -> list[dict]` — читает Excel-файл (`.xlsx`)

### Модуль `processing.py`
- `filter_by_state(transactions: list, state: str) -> list[dict]` — фильтрует транзакции по статусу (`EXECUTED`, `CANCELED`, `PENDING`)
- `sort_by_date(transactions: list, reverse: bool) -> list[dict]` — сортирует транзакции по дате

### Модуль `external_api.py`
- `convert_currency(transaction: dict) -> float` — конвертирует сумму транзакции в рубли через внешнее API (поддерживает USD, EUR)

### Модуль `bank_search.py`
- `process_bank_search(data: list[dict], search: str) -> list[dict]` — ищет транзакции по описанию (регулярные выражения, без учёта регистра)

### Модуль `widget.py`
- `mask_account_card(card_or_account: str) -> str` — маскирует номер карты или счёта
- `get_date(date_str: str) -> str` — преобразует дату из формата ISO в `DD.MM.YYYY`

### Модуль `masks.py`
- `get_mask_card_number(card_number: str) -> str` — маскирует номер карты (формат: `XXXX XX** **** XXXX`)
- `get_mask_account(account_number: str) -> str` — маскирует номер счёта (формат: `**XXXX`)

### Модуль `decorators.py`
- `@log` — логирует вызов функции (в файл или консоль)
- `@retry` — повторяет вызов при ошибке
- `@shorten_words` — обрезает слова в возвращаемом тексте

### Модуль `main.py`
- `main() -> None` — основная логика программы (меню, фильтры, вывод)
- `display_transaction(transaction: dict) -> None` — форматирует и выводит одну транзакцию

### Модуль `generators.py`
- `filter_by_currency(transactions: list, currency: str) -> Iterator[dict]` — фильтрует транзакции по валюте (генератор)
- `transaction_descriptions(transactions: list) -> Iterator[str]` — возвращает описания транзакций (генератор)
- `card_number_generator(start: int, end: int) -> Iterator[str]` — генерирует номера карт в заданном диапазоне
## 🔐 Переменные окружения

Для конвертации валют используется **Exchange Rates Data API** от сервиса [apilayer.com](https://apilayer.com).

Чтобы получить API-ключ:

1. Перейдите на сайт [apilayer.com](https://apilayer.com) и зарегистрируйтесь.
2. Выберите бесплатный тарифный план для **Exchange Rates Data API**.
3. Скопируйте ваш API-ключ из личного кабинета.
4. Создайте в корне проекта файл `.env` и добавьте в него:

## Автор проекта:
Проект создал Галкин Денис Игоревич
## Контактная информация:
email - dis43@mail.ru
.......
