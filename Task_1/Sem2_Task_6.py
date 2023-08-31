# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

from Exeption import InvalidAmountError, InsufficientFundsError

initial_amount = 0
current_amount = initial_amount
transaction_count = 0
tax_rate = 0.1
transaction_limit = 5000

while True:
    print("Сумма денег:", current_amount)
    action = input("Выберите действие (пополнить, снять, выйти): ")

    if action == "выйти":
        print("Программа завершена.")
        break

    elif action == "пополнить":
        try:
            amount = int(input("Введите сумму пополнения: "))
            if amount % 50 != 0:
                raise InvalidAmountError("пополнения")

            current_amount += amount
            transaction_count += 1

            if transaction_count % 3 == 0:
                current_amount *= 1.03

        except InvalidAmountError as e:
            print(e)

    elif action == "снять":
        try:
            amount = int(input("Введите сумму снятия: "))
            if amount % 50 != 0:
                raise InvalidAmountError("снятия")

            if amount > current_amount:
                raise InsufficientFundsError(amount, current_amount)

            if current_amount > transaction_limit:
                current_amount -= current_amount * tax_rate

            commission = amount * 0.015
            commission = max(commission, 30)
            commission = min(commission, 600)

            current_amount -= amount + commission
            transaction_count += 1

        except InvalidAmountError as e:
            print(e)
        except InsufficientFundsError as e:
            print(e)
    else:
        print("Некорректное действие. Попробуйте снова.")
