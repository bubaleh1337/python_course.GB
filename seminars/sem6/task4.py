"""
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n 
(включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. 
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
Программа получает на вход одно натуральное число k, не превосходящее 10^5. Программа должна вывести  
все пары дружественных чисел, каждое из которых не превосходит k.

220 (1 2 4 5 6) 284
284 () 220
"""

num1 = 220
num2 = 284
list1 = []
list2 = []
sum = sum1 = 0
k = 10000

def full(n):
    print(lst := [i for i in range(1, n - 1) if n % i == 0])

# num1:
for i in range(1, num1 - 1): # получаем делитель
    if num1 % i == 0:
        list1.append(i) # добавляем делитель в список
print(list1)

for i in range(len(list1)):
    sum += list1[i] # сумма всех делителей в списке
print(sum)

# num2:

for i in range(1, num2 - 1):
    if num2 % i == 0:
        list2.append(i)
print(list2)

for i in range(len(list2)):
    sum1 += list2[i]
print(sum1)

if sum == num2 and sum1 == num1: # проверка на равенство сумм делителей со вторым числом
    print('friends')

    