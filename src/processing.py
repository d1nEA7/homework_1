def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей по значению EXECUTED"""
    new_list_dict = []
    for item in list_dict:
        if item.get("state") == state:
            new_list_dict.append(item)
    return new_list_dict


def sort_by_date(list_dict: list, reverse=True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    return sorted(list_dict, key=lambda x: x["date"], reverse=reverse)
