a, b, c = list(map(int, input().split()))
summa = a + b + c
proiz = a * b * c
sred = summa / 3
print(a, '+', b, '+', c, '=', summa, sep = '')
print(a, '*', b, '*', c, '=', proiz, sep = '')
print('(', a, '+', b, '+', c, ')', '/3=',"{:5.3f}".format(sred), sep = '')