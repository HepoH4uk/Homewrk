def mask_account_card(account_card = "Maestro 70007922896063657656751"):
    card_num = ""
    card_name = ""
    for i in account_card:
        if i.isdigit():
            card_num+=i
        else:
            card_name += i
    return card_name,card_num

print(mask_account_card("Maestro 70007922896063657656751"))
