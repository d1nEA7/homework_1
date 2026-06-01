from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info_card: str) -> str:
    """ Функция маскировки банковской карты (с названием карты) """
    name_chars = []
    number_chars = []
    for symbol in info_card:
        if symbol.isalpha() or symbol == " ":
            name_chars.append(symbol)
        elif symbol.isdigit():
            number_chars.append(symbol)
    str_name = "".join(name_chars)
    str_chars = "".join(number_chars)
    clean_name = str_name.strip()
    if "Счет" in str_name:
        masked_number = get_mask_account(str_chars)
    else:
        masked_number = get_mask_card_number(str_chars)
    return f"{clean_name} {masked_number}"


def get_date(str_date: str) -> str:
    return f"{str_date[8:10]}.{str_date[5:7]}.{str_date[0:4]}"
