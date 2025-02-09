import json
import logging


logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/utils.log', 'w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def list_transactions(filename="../data/operations.json"):
    """Функция принимающая на вход путь SON-файла и
      возвращает список словарей с данными о финансовых транзакциях"""
    data = []
    try:
        logger.info("Выполняем проверку наименования файла")
        if filename is not None:
            logger.info("Открываем нужный файл")
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        else:
            logger.info("Не указан файл")
            print(data)
        logger.info("Выводим полученный результат")
        return data
    except FileNotFoundError as error:
        logger.error(f"Произошла ошибка: {error}")
        return data
    except json.JSONDecodeError as error:
        logger.error(f"Произошла ошибка: {error}")
        return data
