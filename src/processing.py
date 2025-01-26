def filter_by_state(person_list: list, state: str = 'EXECUTED') -> list:
    """Функция фильтрующая список словарей по значению state"""

    new_person_list = []
    for i in person_list:
        if i.get("state") == state:
            new_person_list.append(i)
    return new_person_list


def sort_by_date(person_list: list, reverse: bool = True) -> list:
    """Функция сортирует список словарей по дате"""

    return sorted(person_list, key=lambda x: x["date"], reverse=reverse)
