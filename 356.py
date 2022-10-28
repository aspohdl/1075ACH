l = 0
res = 0
n, m = map(int, input().split())
for i in range(n):
    a = map(int, input().split())
    a = list(a)
    summa = sum(a)
    if summa > res:
        res = summa
        l = i
print(res)
print(l)