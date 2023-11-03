# 📌 Создайте класс с базовым исключением и дочерние классы-
# исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class ErrorDefault(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return 'Error Default'


class ErrorLevel(ErrorDefault):
    def __str__(self, st) -> str:
        return 'Error Level'


class ErrorAccess(ErrorDefault):
    def __str__(self, st) -> str:
        return 'Error Access'


lev = 8

if lev!=1:
    raise ErrorLevel(f'Уровень доступа не соответствует требуемому - 1. Ваш уровень: {lev}.')
