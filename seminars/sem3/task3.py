"""
Дан список, состоящий из целых чисел. Напишите программу, 
которая подсчитает количество элементов списка, больших предыдущего (элемента с предыдущим номером)
"""

list_num = list(input('Enter numbers '))
count = 0

for i in range(1, len(list_num)):
    if list_num[i - 1] < list_num[i]:
        count += 1
print(list_num, count)
