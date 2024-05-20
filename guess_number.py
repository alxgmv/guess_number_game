# Script generate random secret number from 1 to 100, user must guess that number,
# if the number entered by user is closer that 10 to the secret number, program says "close!"
# if not - "far!". If users next entered number is closer to the secret number, programm says ""closer!
# else - "further!". Once user enters same number as the secret one, programm says "You win!" and stops

import random

secret_num = random.randint(1, 100)
x = abs(int(input("guess a number between 1 and 100: ")))
k = [0]

while x > 100:
    print("please enter a number between 1 and 100")
    x = int(input("guess a number between 1 and 100: "))

while x != secret_num:
    k.append(x)
    if k[-2]:
        if abs(x - secret_num) < abs(k[-2] - secret_num):
            print("closer!")
        else:
            print("further!")
    else:
        if abs(x - secret_num) < 10:
            print("close!")
        else:
            print("far!")
    x = int(input("guess again: "))
print('You win!')
