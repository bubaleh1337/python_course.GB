"""
12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
"""

sum = int(input('Введите сумму двух чисел: '))  # 60
multiply = int(input('Введите произведение двух чисел: '))  # 500
num_x = num_y = 0
i = 0
#while sum != i * multiply:
    
for i in range(sum):
    num_x, num_y = sum - i, sum - num_x
    if sum == num_x + num_y and multiply == num_x * num_y:
        print(f'Загаданные числа {num_x} и {num_y}')
        break
