import random

r = random.randint(1,20)
while True:
    num = input('猜數字:')
    num = int(num)
    if num == r:
        print('bingo!!!')
        break
    elif num > r:
        print('lower')
    elif num < r:
        print('higher')
        