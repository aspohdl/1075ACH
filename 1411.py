input()
a = list(map(int, (input().split())))

def bubl_sort(_list):
   count = 0
   for j in range(len(_list)):
       for i in range(len(_list) - 1, 0, -1):
           if _list[i] < _list[i - 1]:
               count += 1
               _list[i], _list[i - 1] = _list[i - 1], _list[i]
   print(count)

bubl_sort(a)






