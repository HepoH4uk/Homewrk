import re
from collections import Counter

transactions = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
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
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]


descriptions = ["Перевод организации"]
search_string = "Перевод"


def bank_search(transactions, search_string):
    result_data = []
    for transaction in transactions:
        result = re.search(pattern=search_string.lower(), string=transaction["description"].lower(), flags=re.I)
        if result is not None:
            result_data.append(transaction)
    return result_data


def operations_count_by_category(transactions, descriptions):
    """Функция для подсчета количества банковских операций по категориям."""
    category_counter = Counter()
    for transaction in transactions:
        if "description" in transaction:
            description = transaction["description"]
            category_counter[description] += 1
    result = {category: category_counter[category] for category in descriptions}
    return result
