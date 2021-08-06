import random

r = random.randint(1,20)
count = 0
while True:
    num = input('猜數字:')
    num = int(num)
    if num == r:
        print('bingo!!!')
        print('這是第', count, '次')
        break
    elif num > r:
        print('lower')
        count += 1
    elif num < r:
        print('higher')
        count += 1
    print('這是第', count, '次')
        