2. Коротка теорія
2.1. Що таке модуль і бібліотека
Модуль — це Python-файл з готовими функціями, змінними або іншими
об’єктами, які можна використати в іншій програмі. Бібліотека — набір
модулів, призначених для певного кола задач. Використання модулів
дозволяє не писати вже готові алгоритми повторно.
2.2. Способи імпорту
import math
print(math.sqrt(81))
from math import sqrt
print(sqrt(81))
import statistics as stat
print(stat.mean([10, 11, 8, 12]))
Запис Як звертатися Особливість
import math math.sqrt(25) видно, з якого модуля

функція

from math import sqrt sqrt(25) імпортується конкретне

ім’я

import statistics as stat stat.mean(data) короткий псевдонім
2.3. Модуль math
math містить математичні константи та функції. Для цієї роботи важливі pi,
sqrt(), ceil(), floor() і pow().
import math
radius = 5
area = math.pi * radius ** 2
print("Площа круга:", round(area, 2))
print("sqrt(81):", math.sqrt(81))
print("ceil(4.2):", math.ceil(4.2))
print("floor(4.8):", math.floor(4.8))

Сторінка 3

print("pow(2, 5):", math.pow(2, 5))
print("2 ** 5:", 2 ** 5)
math.pow(a, b) повертає результат як float. Оператор ** є універсальним
оператором піднесення до степеня Python і часто зручніший у звичайних
обчисленнях.
2.4. ceil() і floor() у прикладних задачах
ceil() округлює число вгору, floor() — вниз. Наприклад, якщо в одну упаковку
входить 6 предметів, а потрібно запакувати 25, необхідно 5 упаковок.
import math
items = 25
capacity = 6
packages = math.ceil(items / capacity)
print("Потрібно упаковок:", packages)
2.5. Модуль random
random використовують для генерації псевдовипадкових значень. randint(a, b)
повертає ціле число від a до b включно, choice() вибирає випадковий елемент,
shuffle() перемішує список.
import random
print(random.randint(1, 12))
names = ["Anna", "Ivan", "Olha", "Maksym"]
print(random.choice(names))
random.shuffle(names)
print(names)
2.6. Модуль statistics
statistics містить готові функції для базового статистичного аналізу. mean()
обчислює середнє арифметичне, median() — медіану, mode() — найчастіше
значення.

Сторінка 4

import statistics
grades = [10, 8, 12, 10, 9, 10, 11]
print("Середнє:", statistics.mean(grades))
print("Медіана:", statistics.median(grades))
print("Мода:", statistics.mode(grades))
Якщо найчастіше значення не є однозначним або для задачі важливо
отримати всі моди, потрібно уважно перевіряти вимоги задачі та
документацію. Для базових лабораторних mean() і median() є найбільш
передбачуваними.
2.7. Модуль datetime
datetime дозволяє працювати з датами й часом. date.today() повертає поточну
дату, datetime.now() — поточні дату й час. Віднімання двох дат повертає
різницю, з якої можна отримати кількість днів.
from datetime import date, datetime
today = date.today()
now = datetime.now()
print("Сьогодні:", today)
print("Зараз:", now)
2.8. Різниця між датами
from datetime import date
today = date.today()
event = date(2027, 1, 1)
difference = event - today
print("Різниця у днях:", difference.days)
2.9. Власний модуль
Власний модуль — звичайний .py-файл. Наприклад, функції можна винести у
utils.py, а основну програму залишити у main.py.

Сторінка 5

# utils.py
def average(numbers):
return sum(numbers) / len(numbers)
def level(value):
if value >= 10:
return "високий"
if value >= 7:
return "достатній"
return "потребує покращення"
# main.py
import utils
grades = [10, 11, 8, 12]
print(utils.average(grades))
print(utils.level(utils.average(grades)))
2.10. if __name__ == "__main__":
Коли файл запускається безпосередньо, спеціальна змінна __name__ має
значення "__main__". Це дозволяє відокремити код для перевірки модуля від
функцій, які будуть імпортуватися.
def add(a, b):
return a + b

if __name__ == "__main__":
print(add(2, 3))
2.11. Типові помилки
⎯ Імпортовано модуль через import math, але функцію викликають як sqrt()
замість math.sqrt().
⎯ Файл власного модуля має назву, що збігається зі стандартним модулем,
наприклад random.py або math.py.
⎯ У власному модулі залишено код input()/print(), який небажано запускається
одразу під час import.
⎯ Після shuffle() очікують новий список: shuffle() змінює існуючий список.
⎯ Для випадкових даних очікують однаковий результат при кожному запуску.

Сторінка 6

⎯ Плутають date.today() і datetime.now().
⎯ Під час роботи з датами створюють дату як звичайний рядок і намагаються
віднімати рядки.
⎯ Уся логіка залишається в main.py, хоча завдання вимагає створення
власного модуля.
2.12. Графічний інтерфейс із Tkinter
Tkinter — стандартний інтерфейс Python до Tcl/Tk для створення віконних
програм. Замість input() користувач вводить дані в Entry, а замість лише print()
результат можна показувати в Label або Text. Ми створюємо віджети та
звичайні функції def, без написання власних класів.
Перевірка середовища: виконайте python -m tkinter у терміналі (у Windows
також можна py -m tkinter). Має відкритися тестове вікно. У стандартному
інсталяторі Python для Windows підтримка Tcl/Tk зазвичай постачається разом
із Python; у деяких збірках це необов’язковий компонент. Команда pip install
tkinter для стандартного Tkinter не потрібна.
⎯ Tk() створює головне вікно. title() задає заголовок, geometry("400x300") —
початковий розмір.
⎯ Label показує текст; Entry — однорядкове поле; Button — кнопка; Text —
багаторядковий результат.
⎯ pack(pady=5) розміщує елемент із вертикальним відступом. pack() і grid() не
слід змішувати для дочірніх елементів одного контейнера.
⎯ entry.get() повертає рядок. Для обчислень потрібне перетворення int() або
float(). label.configure(text=...) змінює напис.
⎯ command=calculate передає функцію кнопці; command=calculate()
викликає її відразу і є типовою помилкою.
⎯ mainloop() обробляє події до закриття вікна. Довгі цикли й input() всередині
обробника блокують взаємодію.
Приклади Tkinter запускайте по одному. Якщо вони зберігаються послідовно в
class_work.py, кожне наступне вікно відкриється лише після закриття
попереднього. Не називайте файл tkinter.py. Для цієї роботи достатньо
класичних віджетів; ttk можна розглянути пізніше.

Сторінка 7

3. Класна робота: демонстраційні приклади
Приклад 1. math: гіпотенуза і площа круга
import math
a = 6
b = 8
hypotenuse = math.sqrt(a ** 2 + b ** 2)
radius = 5
circle_area = math.pi * radius ** 2
print("Гіпотенуза:", hypotenuse)
print("Площа круга:", round(circle_area, 2))
Приклад 2. ceil() і floor()
import math
items = 25
capacity = 6
print("Повних упаковок:", math.floor(items / capacity))
print("Упаковок потрібно:", math.ceil(items / capacity))
Приклад 3. random.randint(): 10 випадкових чисел
import random
numbers = []
for i in range(10):
numbers.append(random.randint(1, 100))
print(numbers)
Приклад 4. random.choice(): випадковий вибір
import random

Сторінка 8

students = ["Anna", "Ivan", "Olha", "Maksym"]
selected = random.choice(students)
print("Обрано:", selected)
Приклад 5. random.shuffle(): перемішування списку
import random
questions = [1, 2, 3, 4, 5]
random.shuffle(questions)
print("Новий порядок:", questions)
Приклад 6. statistics.mean() і median()
import statistics
grades = [10, 8, 12, 9, 11, 10]
print("Середнє:", statistics.mean(grades))
print("Медіана:", statistics.median(grades))
Приклад 7. Поточна дата і час
from datetime import date, datetime
print("Дата:", date.today())
print("Дата і час:", datetime.now())
Приклад 8. Кількість днів між датами
from datetime import date
date1 = date(2026, 10, 1)
date2 = date(2026, 12, 31)
difference = date2 - date1
print("Днів:", difference.days)

Сторінка 9

Приклад 9. Створення utils.py
# Файл utils.py
def square(number):
return number ** 2
def is_even(number):
return number % 2 == 0

def average(numbers):
return sum(numbers) / len(numbers)
Приклад 10. Імпорт власного модуля
# Файл main.py
import utils
numbers = [4, 8, 10, 12]
print(utils.square(5))
print(utils.is_even(8))
print(utils.average(numbers))
Приклад 11. import math та from math import sqrt
import math
print(math.sqrt(100))
from math import sqrt
print(sqrt(100))
Приклад 12. Міні-проєкт: випадкові оцінки + статистика
import random
import statistics
grades = []
for i in range(20):
grades.append(random.randint(1, 12))

Сторінка 10

print("Оцінки:", grades)
print("Min:", min(grades))
print("Max:", max(grades))
print("Середнє:", round(statistics.mean(grades), 2))
print("Медіана:", statistics.median(grades))
high = 0
for grade in grades:
if grade >= 10:
high += 1
print("Оцінок 10–12:", high)
Приклад 13. Перше вікно Tkinter
import tkinter as tk
# Створення і налаштування вікна
window = tk.Tk()
window.title("Лабораторна No6")
window.geometry("400x200")
label = tk.Label(window, text="Модулі та бібліотеки Python")
label.pack(pady=20)
button = tk.Button(window, text="Закрити",
command=window.destroy)
button.pack(pady=10)
# Очікування натискань і інших подій
window.mainloop()
Приклад 14. Поле введення та кнопка
import tkinter as tk
def greet():
# strip() прибирає зайві пробіли

Сторінка 11

name = name_entry.get().strip()
if name == "":
result.configure(text="Введіть ім’я")
else:
result.configure(text="Вітаю, " + name + "!")
window = tk.Tk()
window.title("Привітання")
window.geometry("400x250")
tk.Label(window, text="Ваше ім’я:").pack(pady=5)
name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=5)
tk.Button(window, text="Привітатися",
command=greet).pack(pady=10)
result = tk.Label(window, text="")
result.pack(pady=5)
window.mainloop()
Приклад 15. Tkinter разом із random та statistics
import tkinter as tk
import random
import statistics
def generate_report():
# Перевіряємо додатне ціле число без try/except
value = count_entry.get().strip()
if not value.isdecimal():
result.configure(text="Введіть ціле число від 1 до
100")
return
count = int(value)
if count < 1 or count > 100:
result.configure(text="Кількість має бути від 1 до
100")

Сторінка 12

return
grades = []
for i in range(count):
grades.append(random.randint(1, 12))
average = statistics.mean(grades)
median = statistics.median(grades)
text = "Оцінки: " + str(grades)
text += "\nСереднє: " + str(round(average, 2))
text += "\nМедіана: " + str(median)
result.configure(text=text)
window = tk.Tk()
window.title("Генератор оцінок")
window.geometry("500x350")
tk.Label(window, text="Кількість оцінок (1–
100):").pack(pady=5)
count_entry = tk.Entry(window)
count_entry.pack(pady=5)
tk.Button(window, text="Згенерувати",
command=generate_report).pack(pady=10)
result = tk.Label(window, text="", wraplength=460,
justify="left")
result.pack(pady=10)
window.mainloop()
