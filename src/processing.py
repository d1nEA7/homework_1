def filter_by_state(list_dict: list, state:str="EXECUTED") -> list:
    new_list_dict = []
    for item in list_dict:
        if item.get("state") == "EXECUTED":


