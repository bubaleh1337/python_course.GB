"""
//2: Найдите сумму цифр трехзначного числа.

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""

n = int(input('Введите 3-х значное число: '))
num = n
sum = 0
if n > 99 and n <= 999:
    while n > 0:
        sum += n % 10
        n //= 10
    print(f'{num} -> {sum}')
else:
    print('Вы ввели не трёхзначное число. Попробуйте снова.')
         
        
