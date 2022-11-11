a = list(input().split())
count = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i+1]:
        count += 1
    else:
        count = count
print(count)





