def ff(a):
    for i in range(2, int((a + 1)**(1/2))):
        if a % i == 0:
            return False
    return True


a = int(input())
if not ff(a):
    print('NO')
else:
    print('YES')
