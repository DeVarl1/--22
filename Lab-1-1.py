# -- coding: utf-8 --
from math import prod
 
arr = [int(input('Введите элемент списка: ')) for i in range(int(input('Введите длину списка: ')))]
print(f'Весь список: {arr}')
print(f'Сумма элементов списка равна: {sum(arr)}')
print(f'Произведение элементов списка: {prod(arr)}')