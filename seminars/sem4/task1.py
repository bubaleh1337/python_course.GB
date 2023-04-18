"""
Напишите программу, которая принимает на вход строку, и отслеживает, 
сколько раз каждый символ уже встречался. Количество повторов добавляется 
к символам с помощью постфикса формата _n.
"""

my_string = list(input("Введите символы: "))

print(my_string[0], end=" ")
for i in range(1, len(my_string)):
		print(f"{my_string[i]}", end=" ")
		count = my_string[:i-1].count(my_string[i])
		if count > 0:
				print(f"_{count}", end=" ")
