import time
from functools import wraps


def log(filename=None):
    """Функция декоратор логирования ошибок и времени работы функций"""
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start = time.time()
            end = time.time()
            success = False

            try:
                result = func(*args, **kwargs)
                end = time.time()
                success = True  # без ошибок

                return result
            except Exception as e:
                success = False  # с ошибкой
                error = e
                end = time.time()
                raise

            finally:
                work_time = round(end - start, 2)
                if success:
                    log_message = f"Функция {func.__name__} выполнялась {work_time} сек. Ошибок нет"
                else:
                    log_message = f"Функция {func.__name__} выполнялась {work_time} сек. Ошибка {error}"
                if filename:  # если есть имя файла
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")

                else:  # если НЕТ имя файла
                    if success:  # без ошибок
                        print(log_message)
                    else:  # с ошибкой
                        print(log_message)

        return inner

    return wrapper
