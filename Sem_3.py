# Задание №3
# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class BaseExcept(Exception):
    pass


class ErrorLevel(BaseExcept):
    pass


class ErrorAccept(BaseExcept):
    pass


try:
    raise ErrorLevel('Ошибка уровня')
except ErrorLevel as exp:
    print(f'Error: {exp}')



try:
    raise ErrorAccept('Ошибка доступа')
except ErrorAccept as exp:
    print(f'Error: {exp}')