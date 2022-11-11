a = list(input().split())
mmax = a[0]
max_count = a.count(mmax)
for i in a:
    if a.count(i) > max_count:
        mmax = i
        max_count = a.count(i)
print(mmax)





