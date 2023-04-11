"""
//11 Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

0 1 1 2 3 5 8 13 21 34 55
0 1 2 3 4 5 6 7  8  9  10
"""

num = int(input('Enter a number: '))
fib = 1
fib_prev = 0

count = 1

while fib < num:
    print(fib, fib_prev)
    temp = fib
    fib += fib_prev
    fib_prev = temp
    count +=1
    print(temp, fib, fib_prev)

print(count)