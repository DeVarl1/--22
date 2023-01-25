# -- coding: utf-8 --
el1 = el2 = 0
a = int(input())

while a != 0:
        if a > el1:
            el2 = el1
            el1 = a
        elif el2 < a:
            el2 = a
a = int(input())
print(el2)