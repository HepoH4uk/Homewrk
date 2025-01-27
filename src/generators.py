def filter_by_currency(transactions, currency):
    for transaction in transactions:
        if transaction["operation_Amount"]["currency"]["name"] == currency:
            yield transaction