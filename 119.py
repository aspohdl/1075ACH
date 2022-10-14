a = int(input())
k1 = 0
count = 0
for k1 in range(1, a+1):
    number = k1
    b = 0
    while number > 0:
        k = number % 10
        number = number // 10
        b = b * 10
        b += k
    if k1 == b:
       count += 1

print(count)
