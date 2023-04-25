"""
22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов 
второго множества. Затем пользователь вводит сами элементы множеств.
"""
from random import randint
size1 = int(input('Введите размер 1-го списка: '))
size2 = int(input('Введите размер 2-го списка: '))

lst1 = [randint(1, 20) for _ in range(size1)]
lst2 = [randint(1, 20) for _ in range(size2)]

print(lst1, lst2)
print(len(set(lst1)), len(set(lst2)))
