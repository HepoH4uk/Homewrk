from src.masks import get_mask_card_number, get_mask_account



def mask_account_card(account_card: str) -> str:
    """Функция обработки информации о картах и счетах"""
    card_num = ""
    card_name = ""

    for i in account_card:

        if i.isdigit():
            card_num += i
        else:
            card_name += i

    if len(card_num) > 17:
        return (f"{card_name} {get_mask_account(card_num)}")
    else:
        return (f"{card_name} {get_mask_card_number(card_num)}")


def get_data(user_date: str) -> str:
    """Функция возвращает дату в корректном формате"""
    new_date = user_date.split("T")
    date = new_date[0].split("-")

    return (f"{date[-1]}.{date[-2]}.{date[-3]}")


print(mask_account_card("Maestro 7000792289606361"))
print(get_data("2024-03-11T02:26:18.671407"))
