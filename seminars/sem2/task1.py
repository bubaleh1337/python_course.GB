"""
По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
Решить задачу используя цикл while

Input:       5

Output:    120
"""

num = int(input('Введите предел факториала: '))

fact = count = 1

if num <= 0:
    print(-1)
else:
    while count <= num:  # 2 <= 5
        fact *= count  # 1 * 2
        count += 1  # 2
    print(fact)

if num <= 0:
    print(-1)
else:
    for i in range(1, num + 1):
        fact *= i
    print(fact)

