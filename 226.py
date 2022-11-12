n = int(input())
s = input()
s = s.split(' ')
b = []
for i in range(0, n):
    b.append(int(s[i]))
x = int(input())
flag = False
for i in range(0, len(b)):
    if b[i] == x:
        print(i + 1, end=' ')
