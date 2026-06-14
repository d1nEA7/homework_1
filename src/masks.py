def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    return f"{card_number[:7]}** ****{card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функцию маскировки номера банковского счета"""
    return f"** {account_number[-4:]}"