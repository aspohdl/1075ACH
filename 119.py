a = int(input())
k1 = 0
count = 0
for k1 in range(1, a+1):
    number = k1
    flip = 0
    while number > 0:
        flip = flip * 10 + number % 10
        number = number // 10
    if k1 == flip:
       count += 1

print(count)
