def get_mask_card_number():
    """Функцию маскировки номера банковской карты"""
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"


def get_mask_account():
    """Функцию маскировки номера банковского счета"""
    assert get_mask_account("73654108430135874305") == "**4305"
