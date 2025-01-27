from typing import Any, Dict, Iterable, Iterator


def filter_by_currency(transactions: Iterable[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Функция возврата транзакций с заданной валютой"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


def transaction_descriptions(transactions: Iterable[Dict[str, Any]]) -> Iterator[Dict[str, Any]]:
    """Функция возврата описания операций"""
    for transaction in transactions:
        descriptions = transaction["description"]
        yield descriptions


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Функция генерирования номера карты"""
    for i in range(start, end + 1):
        card_number = f"{i:016d}"[:4]+" "+f"{i:016d}"[4:8]+" "+f"{i:016d}"[8:12]+" "+f"{i:016d}"[12:16]

        yield card_number
