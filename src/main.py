import json
import csv
import pandas as pd
from src.widget import mask_account_card, get_data
from src.processing import sort_by_date
from src.requests import bank_search


transactions = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Оплата счета",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_csv(file_path):
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        return list(csv.DictReader(csvfile))


def load_xlsx(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")


def main():
    filtered_transactions = []
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла""")

    user_input = int(input())

    if user_input == 1:
        print("Для обработки выбран JSON-файл")
    elif user_input == 2:
        print("Для обработки выбран CSV-файл")
    elif user_input == 3:
        print("Для обработки выбран XLSX-файл")

    state = str(input("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""))
    while state.upper() == "EXECUTED" or "CANCELED" or "PENDING":
        if state.upper() == 'EXECUTED':
            for transaction in transactions:
                if transaction["state"] == 'EXECUTED':
                    filtered_transactions.append(transaction)
            print("Операции отфильтрованы по статусу 'EXECUTED'")
            break
        elif state.upper() == 'CANCELED':
            for transaction in transactions:
                if transaction["state"] == 'CANCELED':
                    filtered_transactions.append(transaction)
            print("Операции отфильтрованы по статусу 'CANCELED'")
            break
        elif state.upper() == 'PENDING':
            for transaction in transactions:
                if transaction["state"] == 'PENDING':
                    filtered_transactions.append(transaction)
            print("Операции отфильтрованы по статусу 'PENDING'")
            break
        else:
            state = input(f"""Статус операции {state} недоступен.
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""")

    date_sort_input = input("Отсортировать операции по дате? Да/Нет").lower()
    if date_sort_input == "да":
        date_sort = input("Отсортировать по возрастанию или по убыванию?").lower()
        if date_sort == "по возрастанию":
            sort_by_date(filtered_transactions, True)
        else:
            sort_by_date(filtered_transactions, False)

    sort_by_rub = input("Выводить только рублевые тразакции? Да/Нет").lower()
    if sort_by_rub == "да":
        filtered_transactions = \
            [transaction
             for transaction in filtered_transactions
             if transaction["operationAmount"]["currency"]["name"] == "руб"]

    need_sort_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
    if need_sort_word == "да":
        sort_word = str(input("Введите слово:\n"))
        filtered_transactions = bank_search(transactions, sort_word)
    print("Распечатываю итоговый список транзакций...")

    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print(f"{get_data(transaction['date'])} {transaction['description']}")
            print(mask_account_card(transaction['to']))
            print(f"Сумма: {transaction["operationAmount"]['amount']} "
                  f"{transaction["operationAmount"]["currency"]["name"]}")
            print()
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == '__main__':
    main()
