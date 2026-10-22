numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]
dodatni = []
vidcemi = []
parni = []
kratni_3 = []
for number in numbers:
  if number > 0:
    dodatni.append(number)
  if number < 0:
    vidcemi.append(number)
  if number % 2 == 0:
    parni.append(number)
  if number % 3 == 0:
    kratni_3.append(number)
min_val = min(numbers)
max_val = max(numbers)
total_sum = sum(numbers)
average = total_sum / len(numbers) if len(numbers) > 0 else 0
print("Додатні:", dodatni)
print("Від'ємні:", vidcemi)
print("Парні:", parni)
print("Кратні 3:", kratni_3)
print(
    f"Min: {min_val}; Max: {max_val}; Sum: {total_sum}; Average:"
    f" {round(average, 2)}"
)




group1 = {"Anna", "Ivan", "Olha"}
group2 = {"Ivan", "Maksym", "Olha"}
spilni = group1 & group2
tільки_group1 = group1 - group2
tільки_group2 = group2 - group1
vsi = group1 | group2
print("Спільні:", ", ".join(sorted(spilni)))
print("Тільки group1:", ", ".join(sorted(tільки_group1)))
print("Тільки group2:", ", ".join(sorted(tільки_group2)))
print("Усі:", ", ".join(sorted(vsi)))



catalog = {"bread": 35, "milk": 48, "cheese": 120, "tea": 75}
low, high = 40, 100
print(f"Ціновий діапазон: {low}..{high} грн")
found_count = 0
for name, price in catalog.items():
  if low <= price <= high:
    print(f"{name} — {price} грн")
    found_count += 1
if found_count == 0:
  print("У заданому діапазоні немає товарів.")




group_info = ("10-IT", "2026/2027")
journal = {}
def add_student(name, grades):
  if len(grades) != 5:
    print(f"Помилка для {name}: учень повинен мати рівно 5 оцінок.")
    return
  is_valid = True
  for grade in grades:
    if not (1 <= grade <= 12):
      is_valid = False
      break
  if is_valid:
    journal[name] = grades
    print(f"Учня {name} успішно додано.")
  else:
    print(
        f"Помилка для {name}: усі оцінки мають бути цілими числами в діапазоні"
        " від 1 до 12."
    )
add_student("Anna", [10, 11, 12, 9, 10])
add_student("Ivan", [8, 9, 10, 11, 9])
print(f"{group_info[0]} — {group_info[1]}")
pairs = []
for name, grades in journal.items():
  grades_str = " ".join(str(g) for g in grades)
  print(f"{name}: {grades_str}")
  avg_score = sum(grades) / len(grades)
  print(f"{name} — {avg_score}")
  pairs.append((avg_score, name))
pairs.sort(reverse=True)
if pairs:
  best_avg, best_name = pairs[0]
  print(f"Найкращий результат: {best_name} — {best_avg}")





