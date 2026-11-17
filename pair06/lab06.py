import math
import random
import statistics
from datetime import date
r = float(input("Радіус: "))
a = float(input("Перший катет: "))
b = float(input("Другий катет: "))
n_items = int(input("Кількість предметів: "))
k_box = int(input("Вмістимість упаковки: "))
area = round(math.pi * r ** 2, 2)
hyp = round(math.sqrt(a ** 2 + b ** 2), 2)
boxes = math.ceil(n_items / k_box)
print("Площа круга:", area)
print("Гіпотенуза:", hyp)
print("Потрібно упаковок:", boxes)





n = int(input("\nКількість оцінок: "))
if n > 0:
    grades = []
    for i in range(n):
        grades.append(random.randint(1, 12))
    high = 0
    for g in grades:
        if g >= 10:
            high += 1
    print("Оцінки:", grades)
    print("Min:", min(grades))
    print("Max:", max(grades))
    print("Середнє:", round(statistics.mean(grades), 2))
    print("Медіана:", statistics.median(grades))
    print("Оцінок 10-12:", high)
else:
    print("Кількість оцінок має бути більшою за 0")







year = int(input("\nРік події: "))
month = int(input("Місяць події: "))
day = int(input("День події: "))

event = date(year, month, day)
today = date.today()
diff = (event - today).days

if diff > 0:
    print("До події залишилося днів:", diff)
elif diff < 0:
    print("Після події минуло днів:", abs(diff))
else:
    print("Подія сьогодні!")




