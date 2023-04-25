"""
39. Даны два массива чисел. Требуется вывести те элементы первого массива 
(в том порядке, в каком они идут в первом массиве), которых нет во втором массиве
"""

import random

list1 = [random.randint(0, 10) for _ in range(5)]
list2 = [random.randint(0, 10) for _ in range(5)]
print(f'{list1} {list2}')
for i in list1:
    if i not in list2:
        print(i, end=" ")

