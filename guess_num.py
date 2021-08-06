import random

start = input('起始值為:')
start = int(start)
end = input('結束值為:')
end = int(end)
r = random.randint(start,end)
count = 0
while True:
    num = input('猜數字:')
    count +=1
    num = int(num)
    if num == r:
        print('bingo!!!')
        print('這是第', count, '次')
        break
    elif num > r:
        print('lower')
    elif num < r:
        print('higher')
    print('這是第', count, '次')
        