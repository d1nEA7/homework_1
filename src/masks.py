import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logs/masks.log",
    filemode="w",
)

get_mask_card_number_logger = logging.getLogger("get_mask_card_number_logger")
get_mask_account_logger = logging.getLogger("get_mask_account_logger")


def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает маску в формате XXXX XX** **** XXXX"""
    get_mask_card_number_logger.info("get_mask_card_number Принимает номер карты")
    if not isinstance(card_number, str):
        get_mask_card_number_logger.warning("номер карты не формата str")
        raise TypeError("Номер карты должен быть строкой")
    if not card_number.isdigit():
        get_mask_card_number_logger.warning("номер карты содержит не только цифры")
        raise ValueError("Номер карты должен содержать только цифры")
    if len(card_number) != 16:
        get_mask_card_number_logger.warning("номер карты не 16 значный")
        raise ValueError("Номер карты должен содержать 16 цифр")

    get_mask_card_number_logger.info("завершение работы get_mask_card_number")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Принимает номер счёта и возвращает маску в формате **XXXX"""
    get_mask_account_logger.info("get_mask_account Принимает номер счёта")
    if not isinstance(account_number, str):
        get_mask_account_logger.warning("Номер счёта не формата str")
        raise TypeError("Номер счёта должен быть строкой")
    if not account_number.isdigit():
        get_mask_account_logger.warning("номер счёта содержит не только цифры")
        raise ValueError("Номер счёта должен содержать только цифры")
    if len(account_number) != 20:
        get_mask_account_logger.warning("номер счёта не 20 значный")
        raise ValueError("Номер счёта должен содержать 20 цифр")
    get_mask_account_logger.info("завершение работы функции get_mask_account")
    return f"**{account_number[-4:]}"
