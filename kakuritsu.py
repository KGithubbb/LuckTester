import random
from random import randint, randrange

I = 0
luck = 0
again = "yes"
while again == "yes":
    luck = 0
    I = 0
    while luck != 1000:
        I = I + 1
        luck = (randint(1,1000))
        if luck == 1000:
            print('1/1000 Youre Luck Is Proved. Kiitos!')
            print(I)
            again = input('Again?: ')
    if again == "no":
        break