a, b = list(map(int, input().split()))
count = 1

while a != b:
    count += 1
    if a > b:
        a = a - b
    else:
        b = b - a

print(a, count)



