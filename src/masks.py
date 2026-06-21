def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает маску в формате XXXX XX** **** XXXX"""
    if not isinstance(card_number, str):
        raise TypeError("Номер карты должен быть строкой")
    if not card_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Принимает номер счёта и возвращает маску в формате **XXXX"""
    if not isinstance(account_number, str):
        raise TypeError("Номер счёта должен быть строкой")
    if not account_number.isdigit():
        raise ValueError("Номер счёта должен содержать только цифры")
    if len(account_number) != 20:
        raise ValueError("Номер счёта должен содержать 20 цифр")

    return f"**{account_number[-4:]}"
