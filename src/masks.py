from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""

    str_card_number = str(card_number)

    if len(str_card_number) == 16:
        return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
    else:
        return "Не верный номер карты"


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковского счета"""

    str_account_number = str(account_number)

    if len(str_account_number) == 20:
        return f"**{str_account_number[-4:-1]}{str_account_number[-1]}"
    else:
        return "Не верный номер банковского счета"
