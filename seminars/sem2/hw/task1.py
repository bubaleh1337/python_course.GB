"""
10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""
import random 

coin = int(input('Введите количество монеток: '))
side_coin = 0
reshka = orel = 0

for i in range(coin):
    side_coin = random.randint(0, 1)
    print(side_coin)
    if side_coin == 0:
        reshka += 1
    else:
        orel += 1
if reshka == 0 or orel == 0:
    print(f'Монет: {coin}, решка: {reshka}, орел: {orel}. Переворачивать нечего.')
elif reshka < orel:
    print(f'Монет: {coin}, решка: {reshka}, орел: {orel}. Перевернём наименьшее количество решек: {reshka}')
elif reshka > orel:
    print(f'Монет: {coin}, решка: {reshka}, орел: {orel}. Перевернём наименьшее количество орлов: {orel}')

else:
    print('Введите натуральное число.')
