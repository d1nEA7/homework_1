# Домашняя работа по теме "обработка банковских операций"

## Описание

Этот проект был создан с целью получения знаний и практики, оттачивания навыков программирования при изучении курсов от онлайн школы программирования "SkyPro". Разработка велась в среде PyCharm.

## Модули проекта

### `src/masks.py`
Функции для маскировки номеров карт и счетов:
- `get_mask_card_number(card_number: str) -> str` — маскирует номер карты (формат: `XXXX XX** **** XXXX`)
- `get_mask_account(account_number: str) -> str` — маскирует номер счета (формат: `**XXXX`)

### `src/widget.py`
Функции для работы с данными:
- `mask_account_card(card_or_account: str) -> str` — определяет тип (карта/счет) и возвращает замаскированный номер
- `get_date(date_str: str) -> str` — преобразует дату из формата ISO в `DD.MM.YYYY`

### `src/processing.py`
Функции для обработки списков транзакций:
- `filter_by_state(transactions: list, state: str = "EXECUTED") -> list` — фильтрует транзакции по статусу
- `sort_by_date(transactions: list, reverse: bool = True) -> list` — сортирует транзакции по дате

### `src/generators.py`
Функции-генераторы для работы с данными:
- `filter_by_currency(transactions: list, currency: str) -> Iterator[dict]` — фильтрует транзакции по валюте
- `transaction_descriptions(transactions: list) -> Iterator[str]` — возвращает описания транзакций
- `card_number_generator(start: int, end: int) -> Iterator[str]` — генерирует номера карт в заданном диапазоне

## Примеры использования

### Маскировка номера карты

```python
from src.masks import get_mask_card_number

print(get_mask_card_number("1234567812345678"))
# 1234 56** **** 5678