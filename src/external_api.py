import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_key")

# Пример транзакции
transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }}


def amount_transactions(transaction):
    """Функция конвертации валюты в рубли"""
    amount = 0
    currency_code = transaction["operationAmount"]["currency"]["code"]
    transaction_amount = transaction["operationAmount"]["amount"]
    url = (f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}"
           f"&from={currency_code}&amount={transaction_amount}")
    headers = {"apikey": f"{API_KEY}"}
    payload = {"amount": transaction_amount, "from": {currency_code}, "to": "RUB"}
    response = requests.get(url, headers=headers, params=payload)
    status_code = response.status_code

    if currency_code == "RUB":
        amount += float(transaction_amount)
        return round(amount, 2)
    else:
        try:
            if status_code == 200:
                data_json = response.json()
                amount += data_json["result"]
                return round(amount, 2)
            else:
                print(status_code)
                print(response.reason)
        except Exception:
            return "Произошла ошибка"


print(amount_transactions(transaction))
