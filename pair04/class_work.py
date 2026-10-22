Приклад 1. Статистика списку оцінок
grades = [10, 8, 12, 9, 11]
print(&quot;Min:&quot;, min(grades))
print(&quot;Max:&quot;, max(grades))
print(&quot;Сума:&quot;, sum(grades))

Сторінка 4

print(&quot;Середнє:&quot;, sum(grades) / len(grades))
Приклад 2. Додавання, видалення та сортування
numbers = [5, 2, 9, 1]
numbers.append(7)
numbers.remove(2)
numbers.sort()
print(numbers)
Приклад 3. Фільтрація у новий список
numbers = [12, -3, 4, -7, 10, 5]
positive = []
for number in numbers:
if number &gt; 0:
positive.append(number)
print(positive)
Приклад 4. Кортеж координат і розпакування
point = (15, -4)
x, y = point
print(&quot;x:&quot;, x)
print(&quot;y:&quot;, y)
Приклад 5. Видалення дублікатів через set
names = [&quot;Ivan&quot;, &quot;Anna&quot;, &quot;Ivan&quot;, &quot;Olha&quot;, &quot;Anna&quot;]
unique_names = set(names)
print(unique_names)
Приклад 6. Спільні елементи двох множин
math = {&quot;Ivan&quot;, &quot;Anna&quot;, &quot;Olha&quot;}
python = {&quot;Anna&quot;, &quot;Maksym&quot;, &quot;Ivan&quot;}
print(&quot;Спільні:&quot;, math &amp; python)
print(&quot;Тільки math:&quot;, math - python)
print(&quot;Усі:&quot;, math | python)
Приклад 7. Словник товарів
prices = {&quot;bread&quot;: 35, &quot;milk&quot;: 48}
prices[&quot;cheese&quot;] = 120
prices[&quot;bread&quot;] = 38
print(prices)
Приклад 8. Перебір items()
prices = {&quot;bread&quot;: 38, &quot;milk&quot;: 48, &quot;cheese&quot;: 120}
for product, price in prices.items():
print(product, &quot;-&quot;, price, &quot;грн&quot;)
Приклад 9. Учень → список оцінок
students = {
&quot;Anna&quot;: [10, 11, 12],

Сторінка 5

&quot;Ivan&quot;: [8, 9, 10]
}
print(students[&quot;Anna&quot;])
Приклад 10. Середній бал кожного учня
students = {
&quot;Anna&quot;: [10, 11, 12],
&quot;Ivan&quot;: [8, 9, 10]
}
for name, grades in students.items():
average = sum(grades) / len(grades)
print(name, round(average, 2))
Приклад 11. Пошук найкращого результату
students = {
&quot;Anna&quot;: [10, 11, 12],
&quot;Ivan&quot;: [8, 9, 10],
&quot;Olha&quot;: [11, 12, 12]
}
best_name = &quot;&quot;
best_average = 0
for name, grades in students.items():
average = sum(grades) / len(grades)
if average &gt; best_average:
best_average = average
best_name = name
print(&quot;Найкращий:&quot;, best_name, round(best_average, 2))
Приклад 12. Вибір структури даних
# list — послідовність оцінок
grades = [10, 8, 12]
# tuple — незмінні координати
point = (10, 20)
# set — унікальні предмети
subjects = {&quot;Python&quot;, &quot;HTML&quot;, &quot;Python&quot;}
# dict — відповідність ключ → значення
student = {&quot;name&quot;: &quot;Ivan&quot;, &quot;grade&quot;: 11}
print(grades, point, subjects, student)
