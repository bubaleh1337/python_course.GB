"""
//4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа 
сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
чем Петя и Сережа вместе?

6 -> 1  4  1
24 -> 4  16  4
  60 -> 10  40  10
"""

sum = int(input('Введите количество сделанных журавлей: '))
man1 = sum // 6
man2 = man1
man3 = (man1 + man2) * 2
print(f'Катя сделала {man3} журавликов, а Петя с Серёжей по {man1}. Общее количество журавликов - {sum}')