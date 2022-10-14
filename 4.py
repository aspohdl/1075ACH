# a=float(input("Введите A "))
# b=float(input("Введите B "))
# if (a == 0) and (b == 0):
#     print("many solutions")
# # elif (b == 0):
# #     print("0")
# elif (a == 0) and (b!=0):
#     print ('no solution')
# elif (b == 0) and (a != 0):
#     print('0')
# elif b%a==0:
#     print(int(b/a))
# else:
#     print('no solution')
a, b = list(map(int, input().split()))

if int(a) == 0:
    if int(b) == 0:
        print('many solutions')
    else:
        print('no solution')
if a != 0:
    if b == 0:
        print(0)
    elif b % a == 0:
        print(int(b//a))
    else:
        print('no solution')


# a = int(input("Введите коэффициент a "))
# b = int(input("Введите коэффициент b "))
# if (a == 0 and b == 0):
#     print("many solutions")
# if (a == 0 and b != 0):
#     print("no solution")
# if (a != 0):
#     print(int(b/a))

