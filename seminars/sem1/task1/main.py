"""
За день машина проезжает n километров. Сколько дней нужно, чтобы 
проехать маршрут длиной m километров? При решении этой задачи 
нельзя пользоваться условной инструкцией if и циклами.
"""

n = int(input('Введите километры за день: '))
m = int(input('Введите длину маршрута в километрах: '))
days = m / n
print(f'Дней для прохождения маршрута: {days}')