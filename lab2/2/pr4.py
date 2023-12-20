from random import randint
from time import time

computer_random = randint(1,500)
change = 0
start_time = time()



while True:
    user_input = input("Введите вашу попытку(для выоха введите 0:")

    if user_input =="0":
        print("Выход из игры")
        break

    try:
        guess = int(user_input)
        change += 1
        if guess < computer_random:
            print("Загаданное число больше")
        elif guess > computer_random:
            print("Заданное число меньше")
        else:
            end_time = time()
            print(f"Вы угадали число {computer_random} за {change} попыток и {round(end_time - start_time)} секунд")
            break
    except ValueError:
        print("Введите коректное число")





