class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Недостаточно средств на счете. Запрошенная сумма: {amount}, текущий баланс: {balance}")

class InvalidAmountError(Exception):
    def __init__(self, amount_type):
        self.amount_type = amount_type
        super().__init__(f"Сумма {amount_type} должна быть кратной 50 у.е.")

class InvalidRectangleError(Exception):
    def __init__(self, height, width=None):
        if width is None:
            message = f"Ошибка: Некорректный прямоугольник: высота={height}, ширина={width}. Ширина не может быть пустой."
        else:
            message = f"Ошибка: Некорректный прямоугольник: высота={height}, ширина={width}. Высота и ширина должны быть положительными целыми числами."
        super().__init__(message)


class UnsupportedOperationError(Exception):
    def __init__(self, operation):
        message = f"Ошибка: Неподдерживаемая операция: {operation}. Эта операция не поддерживается для прямоугольников."
        super().__init__(message)