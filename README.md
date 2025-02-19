# Учебный проект по Python

## Маскировка банковских данных

Программа предназначена для маскировки банковских номеров и счетов, а также для вывода даты в корректном формате. Она позволяет скрыть конфиденциальную информацию о банковских счетах и номерах, делая их трудночитаемыми для посторонних лиц.  

### Установка

Склонируйте репозиторий и добавьте его себе
```
git clone git@github.com:HepoH4uk/Homewrk.git
```
### Использование

Для маскировки банковского номера или счета используйте файл `widget.py`, он также вернет дату в корректном формате

Для фильтра списка словарей по значению и сортировке их по дате используйте файл `processing.py`

### Пример
Ввод
```
print(mask_account_card("Maestro 7000792289606361"))
print(get_data("2024-03-11T02:26:18.671407"))
```
Вывод
```
Maestro  7000 79** **** 6361
11.03.2024
```
## Декорирование функций
Ввод
```
my_function(1, "0")
```
Вывод
```
my_function error: unsupported operand type(s) for /: 'int' and 'str'. Inputs: (1, '0'), {}
```

## Обработка JSON файлов благодаря utils.py

Функция принимающая на вход путь SON-файла и возвращает список словарей с данными о финансовых транзакциях

## Конвертация валюты в рубли благодаря external_api.py
Для конвертации валюты пользуемся Exchange Rates Data API
Токен доступа для API можно получить тут:
```
https://apilayer.com/marketplace/exchangerates_data-api
```

## Чтение 'csv' и 'excel' файлов
Функция read_file_csv помогает прочитать csv-файл и возвращает список словарей
Функция read_file_excel помогает прочитать excel-файл и возвращает список словарей
При возникновении различных ошибок будет выводиться пустой список

## Тестирование функций

Для всех функций добавлены проверочные тесты
```
test_masks.py
test_processing.py
test_widget.py
test_generators.py
test_decorators.py
test_external_api.py
test_utils.py
test_read_cvs_excel.py
```
