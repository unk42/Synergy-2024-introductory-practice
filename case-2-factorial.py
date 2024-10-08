import math

# Простое вычисление факториала положительных целых чисел.

'''Функция, отвечающая за получение от пользователя ввода числа
и проверяющая его корректность.'''
def get_positive_integer():
    while True:
        try:
            num = int(input("Введите положительное целое число: "))
            if num <= 0:
                print("Ошибка: Введите положительное число.")
            else:
                return num
        except ValueError:
            print("Ошибка: Введите целое число.")

# Непосредственное вычисление факториала
def calculate_factorial(n):
    return math.factorial(n)

# Основное тело программы
def main():
    num = get_positive_integer()
    factorial = calculate_factorial(num)
    print(f"Факториал числа {num} равен {factorial}")

# Запуск основного тела программы
if __name__ == "__main__":
    main()
