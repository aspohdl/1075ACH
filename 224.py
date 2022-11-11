input()
a = map(int, (input().split()))
n = int(input())
k = 0
for i in a:
    if i == n:
        k += 1

if k != 0:
    print('YES')
else:
    print('NO')





