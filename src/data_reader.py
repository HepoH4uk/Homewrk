import csv
import pandas as pd


def read_file_csv(file):
    """Считываем csv-файл и возвращаем список словарей"""
    transactions = []
    try:
        with open(file, encoding='utf-8') as st_file:
            reader = csv.DictReader(st_file, delimiter=";")

            for row in reader:
                transactions.append(row)
            return transactions
    except FileNotFoundError:
        return []


def read_file_excel(file):
    """Считываем excel-файл и возвращаем список словарей"""
    df = pd.read_excel(file)
    transactions = df.to_dict(orient='records')
    return transactions
