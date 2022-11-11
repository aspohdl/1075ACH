input()
a = map(int, (input().split()))
n = int(input())
k = 0
for i in a:
    if i == n:
        k += 1
print(k)





