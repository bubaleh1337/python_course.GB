"""
12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
"""

num_x = int(input('Введите первое число не больше 1000: '))
num_y = int(input('Введите второе число не больше 1000: '))
sum = num_x + num_y
multiply = num_x * num_y

if num_x <= 1000 and num_y <= 1000:
    print(f'Сумма загаданных чисел: {sum}, произведение: {multiply}, загаданные числа {num_x} и {num_y}')
else:
    print('Пожалуйста, задумайте число не больше 1000.')
