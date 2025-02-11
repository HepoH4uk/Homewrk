import logging
from typing import Union


logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/masks.log', 'w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""

    str_card_number = str(card_number)
    logger.info("Выполняем проверку длинны номера карты")
    try:
        if len(str_card_number) == 16:
            logger.info("Выводим полученный результат")
            return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
        else:
            logger.info("Не корректный номер карты")
            return "Не верный номер карты"
    except Exception as error:
        logger.error(f"Произошла ошибка: {error}")
        return "Произошла ошибка"


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковского счета"""

    str_account_number = str(account_number)
    logger.info("Выполняем проверку длинны номера счета")
    try:
        if len(str_account_number) == 20:
            logger.info("Выводим полученный результат")
            return f"**{str_account_number[-4:-1]}{str_account_number[-1]}"
        else:
            logger.info("Не корректный номер счета")
            return "Не верный номер банковского счета"
    except Exception as error:
        logger.error(f"Произошла ошибка: {error}")
        return "Произошла ошибка"
