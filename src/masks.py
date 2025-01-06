from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""

    str_card_number = str(card_number)

    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковского счета"""

    str_account_number = str(account_number)

    return f"**{str_account_number[-5:-1]}"
