import random

length = 30
count = 0
max_count = 0
today = 0

for i in range(length):
		today += random.randint(-3, 3)
		print(today, end=" ")
		if today > 0:
				count += 1
				if count > max_count:
						max_count = count
		else:
				count = 0
print(f"\nМаксимальное число тёплых дней: {max_count} дней (день/дня)")