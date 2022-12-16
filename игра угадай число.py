print('Угадай число от 1 до 100!')
import random
n = int(input())
x = random.randint(1, 100)
s = 0

while x > n:
    print('больше бро')
    n = int(input())
    s += 1
    if s > 9:
        print('ALL MY FRIENDS ARE TOXIC... ты проиграл')
        exit()
while x < n:
    print('меньшеее!!!')
    n = int(input())
    s += 1
    if s > 9:
        print('ALL MY FRIENDS ARE TOXIC... ты проиграл')
        exit()
print('УРА ПОБЕДА')




