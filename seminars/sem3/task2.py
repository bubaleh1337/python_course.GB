"""
Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, 
K – положительное число.
"""

list_num = list(input('Enter numbers '))
k = int(input('Enter k '))
list_new = list_num[-k:] + list_num[:-k]
print(list_num)
print(list_new)
