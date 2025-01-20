from src.masks import get_mask_card_number, get_mask_account
import pytest


def tests_mask():
    assert get_mask_card_number("") == "Не верный номер карты"
    assert get_mask_card_number(4635867521348765) == "4635 86** **** 8765"
    assert get_mask_card_number(423) == "Не верный номер карты"

    assert get_mask_account("") == "Не верный номер банковского счета"
    assert get_mask_account(46358675213487659870) == "**9870"
    assert get_mask_account(45678) == "Не верный номер банковского счета"


@pytest.mark.parametrize("card_number, mask_card_number", [
    ("9876245397868907", "9876 24** **** 8907"),
    ("2435876512430798", "2435 87** **** 0798"),
    ("24358765465312430798", "Не верный номер карты"),
    ("", "Не верный номер карты")
])
def test_get_mask_card_number(card_number,mask_card_number):
    assert get_mask_card_number(card_number) == mask_card_number


@pytest.mark.parametrize("account_number, mask_account_number", [
    ("08791243976824537465", "**7465"),
    ("46532453908786574376", "**4376"),
    ("2435876", "Не верный номер банковского счета"),
    ("", "Не верный номер банковского счета")
])
def test_get_mask_account_number(account_number,mask_account_number):
    assert get_mask_account(account_number) == mask_account_number

@pytest.fixture()
def tests_account_masks():
    return "**9870"

def tests_masks_account(tests_account_masks):
    assert get_mask_account("46358675213487659870") == tests_account_masks


@pytest.fixture()
def tests_card_masks():
    return "4635 86** **** 8765"

def tests_masks_card(tests_card_masks):
    assert get_mask_card_number("4635867521348765") == tests_card_masks







