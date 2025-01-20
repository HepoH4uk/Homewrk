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

print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
))