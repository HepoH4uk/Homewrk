from src.requests import bank_search, operations_count_by_category


def test_operations_count_by_category():
    transactions = [
        {"id": 1, "description": "Перевод организации", "amount": 100},
        {"id": 2, "description": "Оплата ЖКХ", "amount": 1500},
        {"id": 3, "description": "Перевод со счета на счет", "amount": 450},
        {"id": 4, "description": "Перевод организации", "amount": 250},
    ]

    categories = [
        "Перевод организации",
        "Оплата ЖКХ",
        "Перевод со счета на счет",
    ]

    expected_result = {
        "Перевод организации": 2,
        "Оплата ЖКХ": 1,
        "Перевод со счета на счет": 1,
    }

    result = operations_count_by_category(transactions, categories)

    assert result == expected_result


def test_bank_search():
    transactions = [
        {"id": 1, "description": "Оплата парковки", "amount": 100},
        {"id": 2, "description": "Оплата ЖКХ", "amount": 1500},
        {"id": 3, "description": "Штраф", "amount": 450},
        {"id": 4, "description": "Перевод организации", "amount": 250},
    ]
    search_string = "Перевод"
    expected_result = [
        {"id": 4, "description": "Перевод организации", "amount": 250}
    ]

    result = bank_search(transactions, search_string)

    assert result == expected_result
