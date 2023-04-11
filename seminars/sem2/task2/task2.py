"""
Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это 
самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, 
а те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, 
в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
"""

import random

length = 30
day = 0

count = 0
count_max = 0

while day < length:
    gradus = random.randint(-5, 5)
    print(day + 1, gradus)
    if gradus > 0:
        count += 1
    else:
        count = 0
    if count > count_max:
        count_max = count
    day += 1

print(count_max)