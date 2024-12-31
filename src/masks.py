from typing import Union
from widget import mask_account_card

def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""

    str_card_number = str(card_number)

    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковского счета"""

    str_account_number = str(account_number)

    return f"**{str_account_number[-5:-1]}"

card_name, card_num = mask_account_card()

if len(card_num)<17:
    print(f"{card_name} {get_mask_account(card_num)}")
else:
    print(f"{card_name} {get_mask_card_number(card_num)}")
