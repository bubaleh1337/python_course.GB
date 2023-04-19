"""
25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

Для решения данной задачи используйте функцию .split()
"""

text = input('Введите строку: ').split()

count = {}

for letter in text:
    count[letter] = count.get(letter, 0) + 1
    if count.get(letter) == 1: print(f'{letter}')
    else: print(f'{letter}_{count.get(letter)}', end=" ")
