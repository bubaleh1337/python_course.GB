"""
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве 
определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
"""

import random

list1 = [random.randint(0, 10) for _ in range(5)]
print(list1)
count_ = 0
for i in range(len(list1[1:-2])):
    if list1[i-1] < list1[i] and list1[i+1] < list1[i]:
        count_+=1
print(count_)
