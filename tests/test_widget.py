import pytest
from src.widget import mask_account_card, get_data


@pytest.mark.parametrize("account_card, mask_account", [
    ("Maestro 7000792289606361", "Maestro  7000 79** **** 6361"),
    ("Visa Platinum 7000792289606361", "Visa Platinum  7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет  **4305"),
    ("", "Данные введены некорректно"),
    ("23453245", "Данные введены некорректно")
])
def test_mask_account_card(account_card,mask_account):
    assert mask_account_card(account_card) == mask_account


@pytest.mark.parametrize("user_date, correct_date", [
    ("2022-06-11T02:26:18.671407", "11.06.2022"),
    ("2015-12-23T02:26:18.671407", "23.12.2015"),
])
def test_get_data(user_date,correct_date):
    assert get_data(user_date) == correct_date


@pytest.fixture()
def get_data_test():
    return "11.06.2022"


def test_get_data_test(get_data_test):
    assert get_data("2022-06-11T02:26:18.671407") == get_data_test

@pytest.fixture()
def card_account():
    return "Maestro  7000 79** **** 6361"

def test_mask_card(card_account):
    assert mask_account_card("Maestro 7000792289606361") == card_account