# Author: pytnproject

import random

while True:
    try:
        user_input = int(input("Мы играем с ограниченными попытками или без?\n[1] — Без ограничений\n[2] — С ограничениями\nВаш ответ: "))
        if user_input == 1:
            difficult = False
            break
        elif user_input == 2:
            difficult = True
            break
        else:
            print("Выбирайте между 1 и 2!")       
    except ValueError:
        print("Выбирайте между 1 и 2!")   

while not difficult:
    secret = random.randint(1,100)
    attempts = 0
    while True:
        try:
            guess = input("\nУгадай число: ")
            guess = int(guess)
            attempts += 1
        except ValueError:
            print ("\nЭто не число!\n")
            continue
        if guess > secret:
            print("\nМеньше!")
        elif guess < secret:
            print("\nБольше!")
        else:
            print(f"\nВы угадали, правильное число {secret}. Вы потратили {attempts} попыток!\n")
            break
    if input("Играем ещё раз? (да/нет): ").strip().lower() != "да":
        break
        
while difficult:
    secret = random.randint(1,100)
    attempts = 10
    count = 0
    guess = None
    while attempts != 0:
        try:
            guess = input(f"\nУгадай число! Попыток осталось {attempts}: ")
            guess = int(guess)
            attempts -= 1
            count += 1
        except ValueError:
            print (f"\nЭто не число! Попыток осталось: {attempts}\n")
            continue
        if guess > secret:
            print(f"\nМеньше!\n")
        elif guess < secret:
            print(f"\nБольше!\n")
        else:
            print(f"\nВы угадали, правильное число {secret}. Вы потратили {count} попыток!\n")
            break
    if guess != secret:
       print(f"Попытки закончились! Правильное число: {secret}")    
    if input("Играем ещё раз? (да/нет): ").strip().lower() != "да":
        break