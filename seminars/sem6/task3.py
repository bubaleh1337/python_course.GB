"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках.
"""

from random import randint

list1 = list2 = [randint(0, 10) for _ in range(10)]

pair = 0
print(list1)
for i in range(len(list1)):
    for j in range(len(list2[:i])):
        if list1[i] == list2[j]:  # and i != j:
            pair += 1
            break

print(pair)
