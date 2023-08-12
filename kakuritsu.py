import random
from random import randint, randrange

I = 0
Castoria = 0
again = "yes"
while again == "yes":
    Castoria = 0
    I = 0
    while Castoria != 1000:
        I = I + 1
        Castoria = (randint(1,1000))
        if Castoria == 1000:
            print('1/1000 Youre Luck Is Proved. Kiitos!')
            print(I)
            again = input('Again?: ')
    if again == "no":
        break