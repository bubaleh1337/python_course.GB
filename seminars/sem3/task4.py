"""
Напишите программу для печати всех уникальных значений в словаре.

my_list = [{"V": "S001"}, {"V": "S002"},
          {"VI": "S001"}, {"VI": "S005"},
          {"VII": "S005"}, {" V ": "S009"},
          {" VIII ": "S007"}]
"""

my_list = [{"V": "S001"}, {"V": "S002"},
           {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {" V ": "S009"},
           {" VIII ": "S007"}]
list_new = set()

for item in my_list:
    for v in item.values():
        list_new.add(v)

print(list_new)
