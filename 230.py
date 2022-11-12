n = int(input())
s = input()
s = s.split(' ')
b = []
for i in range(0, n):
    b.append(int(s[i]))
z = 0
for i in range(0, n):
    max = -1001
    for j in range(0, n - i):
        if max < b[j]:
            max = b[j]
            z = j
    b[z], b[len(b) - 1 - i] = b[len(b) - 1 - i], b[z]
print(*b)
