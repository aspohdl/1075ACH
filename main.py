n = input()
count = 1
max_count = 0
for i in range(len(n)-1):
    if n[i] == n[i+1]:
        count += 1
        max_count = max(count, max_count)
    else:
        count = 1
if max_count >= 2:
    print('YES')
else:
    print('NO')






