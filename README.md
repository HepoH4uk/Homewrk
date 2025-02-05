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

## Тестирование функций

Для всех функций добавлены проверочные тесты
```
test_masks.py
test_processing.py
test_widget.py
test_generators
test_decorators
```
