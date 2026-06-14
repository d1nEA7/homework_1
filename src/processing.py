def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей по значению EXECUTED"""
    new_list_dict = []
    for item in list_dict:
        if item.get("state") == state:
            new_list_dict.append(item)
    return new_list_dict


def sort_by_date(transactions: list, reverse: bool = True) -> list:
    """Возвращает новый список, отсортированный по дате"""
    if not isinstance(transactions, list):
        raise TypeError("На вход должен подаваться список")

    for item in transactions:
        if not isinstance(item, dict):
            raise TypeError("Каждый элемент списка должен быть словарём")
        if "date" not in item:
            raise KeyError("В словаре отсутствует ключ 'date'")
        if not isinstance(item["date"], str):
            raise TypeError("Значение 'date' должно быть строкой")
        # Проверка формата YYYY-MM-DD...
        date_str = item["date"]
        if len(date_str) < 10 or date_str[4] != '-' or date_str[7] != '-':
            raise ValueError("Некорректный формат даты")

    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)