# -- coding: utf-8 --
# е1 - максимальное число
# е2 - второе (меньше е1)) максимальное
el1 = el2 = 0
a = int(input())
# цикл - пока "а" не равно 0
while a != 0:
    # если введенное число больше максимума
    if a > el1:
    # второй максимум равен первому
        el2 = el1
    # а первый максимум равен введенному числу
        el1 = a
    # иначе, если введенное больше второго максимума
    elif el2 < a:
    # то второй максимум становится равным введенному
    # а первый максимум остается неизменным
        el2 = a
    # следующее вводимое число
    a = int(input())
print(el2)