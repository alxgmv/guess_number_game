import random

secret_num = 67
#random.randint(1, 100)
x = abs(int(input("guess a number between 1 and 100: ")))
k = [0]

while x > 100 :
    print("please enter a number between 1 and 100")
    x = int(input("guess a number between 1 and 100: "))

while x != secret_num:
    k.append(x)
    if k[-2] :
        if abs(x - secret_num) < abs(k[-2] - secret_num):
            print("closer!")
        else:
            print("farther!")
    else:
        if abs(x - secret_num) < 10:
            print("close!")
        else:
            print("far!")
    x = int(input("guess again: "))    
print('You win!')