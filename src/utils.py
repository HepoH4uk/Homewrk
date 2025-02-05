import json


def list_transactions(filename="../data/operations.json"):
    """Функция принимающая на вход путь SON-файла и
      возвращает список словарей с данными о финансовых транзакциях"""
    data = []
    try:
        if filename is not None:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        else:
            print(data)
        return data
    except Exception:
        return data


print(list_transactions())
