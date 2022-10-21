i = 2
k = 0
n = int(input())
while 1:
    if (i**2 - i*2) - k <= n <= i**2:
        break
    else:
        i += 1
        k += 1
if n == 1:
    print(3)
elif n == i ** 2:
    print(n-1, n+(i*2))
elif n == (i**2 - i) - k:
    print(n+1, n+(i*2))
else:
    print(n - ((i-1)*2), n-1, n+1, n+(i*2))
