import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions


@pytest.fixture
def usd_transactions():
    return list(filter_by_currency(transactions, "USD"))


@pytest.fixture
def rub_transactions():
    return list(filter_by_currency(transactions, "RUB"))


@pytest.mark.parametrize("states", [("EXECUTED", "CANCELED")])
def test_filter_by_currency(states):
    if states == "EXECUTED":
        assert len(usd_transactions) == 2
        assert "USD" in usd_transactions[0]["operationAmount"]["currency"].values()
        assert "USD" in usd_transactions[1]["operationAmount"]["currency"].values()

    elif states == "CANCELED":
        assert len(rub_transactions) == 2
        assert "RUB" in rub_transactions[0]["operationAmount"]["currency"].values()
        assert "RUB" in rub_transactions[1]["operationAmount"]["currency"].values()


@pytest.mark.parametrize(
    "data, expected", [([{"description": "Перевод организации", },
                         {"wrong_key": "Перевод со счета на счет", },
                         {"description": "Перевод с карты на карту", }, ],
                        ["Перевод организации", "", "Перевод с карты на карту"]),
                       ([], [])]
)
def test_transaction_descriptions(data, expected):
    assert list(transaction_descriptions(data)) == expected


@pytest.mark.parametrize('start, stop, expected', [
    (1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003",
            "0000 0000 0000 0004", "0000 0000 0000 0005"]),
    (111110, 111115, ["0000 0000 0001 1110", "0000 0000 0001 1111",
                      "0000 0000 0001 1112", "0000 0000 0001 1113",
                      "0000 0000 0001 1114", "0000 0000 0001 1115"])
])
def test_card_number_generator(start, stop, expected):
    expected_result = ["0000 0000 0001 1110", "0000 0000 0001 1111", "0000 0000 0001 1112",
                       "0000 0000 0001 1113", "0000 0000 0001 1114", "0000 0000 0001 1115"]

    general_result = list(card_number_generator(start, stop))

    if general_result != expected_result:
        print(
            f"Ошибка: Не совпадают результаты.\n"
            f"Ожидалось: {expected_result}\n"
            f"Получено: "f"{general_result}")
