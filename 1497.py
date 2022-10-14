a, b = list(map(int, input().split()))

if int(a) == 0:
    if int(b) == 0:
        print('many solutions')
    else:
        print('no solution')
if a != 0:
    if b == 0:
        print(0)
    elif b % a == 0:
        print(int(b//a))
    else:
        print('no solution')

