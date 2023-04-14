"""
Дан список чисел. Определите, сколько в нем встречается различных чисел.
"""

list_num = list(input('Введите список чисел: '))

uniq_list = []
for item in list_num:
    if not item in uniq_list:
        uniq_list.append(item)
print(list_num)
print(uniq_list)
print(len(uniq_list))
