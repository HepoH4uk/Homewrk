from functools import wraps


def log(filename = None):
    """Декоратор логирования функции, а также ее результаты или возникшие ошибки"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok" + "\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as error:
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {str(error)}. Inputs: {args}, {kwargs}" + "\n")
                else:
                    print(f"{func.__name__} error: {str(error)}. Inputs: {args}, {kwargs}")
                raise error
        return wrapper
    return decorator

#Пример использования декоратора
@log(filename="mylog.txt")
def my_function(x, y):
    return x / y

my_function(1, 2)