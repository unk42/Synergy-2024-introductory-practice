import random
import time

def play_game():
    print('Я загадаю число от одного до... "Введите предельно возможное число:"')
    diapazon = int(input())
    number_to_guess = random.randint(1, diapazon)
    attempts = 10
    print(f"Я загадал число от 1 до {diapazon}. У вас есть {attempts} попыток, чтобы угадать.")

    while attempts > 0:
        guess = input("Введите вашу догадку: ")

        if not guess.isdigit():
            print("Пожалуйста, введите целое число.")
            continue

        guess = int(guess)

        if guess < number_to_guess:
            print("Слишком маленькое число. Попробуйте еще раз.")
        elif guess > number_to_guess:
            print("Слишком большое число. Попробуйте еще раз.")
        else:
            print(f"Поздравляю! Вы угадали число {number_to_guess} за {11 - attempts} попыток(попытки).")
            break

        attempts -= 1
        print(f"Число оставшихся попыток: {attempts}")

    if attempts == 0:
        print(f"Игра окончена. Загаданное число было {number_to_guess}.")

    play_again = input('Хотите сыграть еще раз? (введите "да" для продолжения): ')
    if play_again.lower() == "да":
        play_game()
    else:
        print("Спасибо за игру! До свидания.")

print("Добро пожаловать в игру 'Угадай число'!")

time.sleep(2)

play_game()
