from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_or_account: str) -> str:
    """Принимает строку с названием и номером карты/счёта, возвращает строку с замаскированным номером"""
    parts = card_or_account.rsplit(" ", 1)
    if len(parts) != 2:
        return card_or_account

    title, number = parts
    if len(number) == 16:
        masked_number = get_mask_card_number(number)
    elif len(number) == 20:
        masked_number = get_mask_account(number)
    else:
        return card_or_account

    return f"{title} {masked_number}"


def get_date(date_str: str) -> str:
    """Принимает дату в формате YYYY-MM-DDTHH:MM:SS, возвращает в формате DD.MM.YYYY"""
    if date_str is None:
        raise ValueError("Дата не может быть None")
    if not isinstance(date_str, str):
        raise ValueError("Дата должна быть строкой")

    if len(date_str) < 10 or date_str[4] != '-' or date_str[7] != '-':
        raise ValueError("Некорректный формат даты")

    # Если длина больше 10, следующий символ должен быть 'T' (иначе ошибка)
    if len(date_str) > 10 and date_str[10] != 'T':
        raise ValueError("Некорректный формат даты")

    # Если длина ровно 10, но тест ожидает ошибку — добавим проверку на отсутствие времени
    if len(date_str) == 10:
        raise ValueError("Некорректный формат даты (отсутствует время)")

    try:
        return f"{date_str[8:10]}.{date_str[5:7]}.{date_str[0:4]}"
    except IndexError:
        raise ValueError("Некорректный формат даты")