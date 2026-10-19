1. Що потрібно повторити
 Тип str та Unicode.
 len().
 Індекси 0..n-1 і від’ємні індекси.
 Незмінність рядків.
 Зрізи [start:end:step].
 Перебір символів циклом for.
 Оператор in.
 lower(), upper(), title(), capitalize().
 strip(), lstrip(), rstrip().
 find(), count(), replace().
 startswith(), endswith().
 isalpha(), isdigit(), isalnum().
 split(), join().
 ord(), chr() як розширення.
 Форматування результатів f-рядками.
2. Коротка теорія
2.1. Рядок як послідовність символів
Рядок (str) — це послідовність Unicode-символів. До окремих символів можна звертатися за
індексом. Перший символ має індекс 0, останній можна отримати через індекс -1.
text = &quot;Python&quot;
print(text[0]) # P
print(text[-1]) # n
print(len(text)) # 6
Запис Значення для &#39;Python&#39;
text[0] P
text[2] t
text[-1] n
len(text) 6
2.2. Зрізи
Зріз дозволяє отримати частину рядка. Загальна форма: text[start:end:step]. Символ з індексом
end у результат не входить.

Сторінка 2

text = &quot;Programming&quot;
print(text[0:7])
print(text[::2])
print(text[::-1])
2.3. Рядки незмінні
Символ у рядку не можна замінити присвоєнням text[0] = &#39;A&#39;. Методи рядків повертають новий
рядок, тому результат потрібно зберегти або одразу використати.
text = &quot; python &quot;
clean_text = text.strip()
upper_text = clean_text.upper()
print(clean_text)
print(upper_text)
2.4. Основні методи рядків
Метод Призначення
lower() / upper() зміна регістру
title() / capitalize() оформлення слів/речення
strip() видалення пробілів по краях
find() пошук позиції підрядка
count() кількість входжень
replace() заміна частини тексту
startswith() / endswith() перевірка початку/кінця
isalpha() чи складається рядок з літер
isdigit() чи складається рядок з цифр
split() рядок → частини
join() частини → рядок
2.5. Перебір символів
Рядок можна перебирати циклом for. Це зручно для підрахунку літер, цифр, пробілів, голосних та
інших символів.
text = input(&quot;Введіть текст: &quot;)
digits = 0
for char in text:
if char.isdigit():
digits += 1
print(&quot;Цифр:&quot;, digits)
2.6. split() і join()
split() розбиває текст на частини та повертає список рядків. join() виконує зворотну операцію —
об’єднує рядки через заданий роздільник.
sentence = &quot;Python is easy&quot;
words = sentence.split()
print(words)
result = &quot; | &quot;.join(words)
print(result)

Сторінка 3

2.7. ord() і chr()
ord() повертає числовий код символу Unicode, а chr() — символ за кодом. Це можна використати
для простих алгоритмів перетворення символів.
letter = &quot;A&quot;
code = ord(letter)
print(code)
print(chr(code + 1))
2.8. Типові помилки
 Звернення до індексу, якого не існує.
 Спроба змінити окремий символ рядка через присвоєння.
 Забутий результат strip(), lower(), replace() — початковий рядок сам не змінюється.
 Неправильне розуміння меж зрізу: end не включається.
 Підрахунок слів через пробіли замість split(), що дає помилки при кількох пробілах.
 Порівняння тексту без попередньої нормалізації регістру та пробілів.
3. Класна робота: демонстраційні приклади
Приклад 1. Перший і останній символ
text = input(&quot;Введіть слово: &quot;)
print(&quot;Перший:&quot;, text[0])
print(&quot;Останній:&quot;, text[-1])
Приклад 2. Зрізи рядка
text = &quot;Programming&quot;
print(text[:7])
print(text[3:8])
print(text[::2])
Приклад 3. Розворот рядка
text = input(&quot;Текст: &quot;)
print(text[::-1])
Приклад 4. Підрахунок голосних, цифр і пробілів
text = input(&quot;Введіть текст: &quot;)
vowels = &quot;аеєиіїоуюяaeiou&quot;
vowel_count = 0
digit_count = 0
space_count = 0
for char in text.lower():
if char in vowels:
vowel_count += 1
if char.isdigit():
digit_count += 1
if char == &quot; &quot;:
space_count += 1

Сторінка 4

print(&quot;Голосних:&quot;, vowel_count)
print(&quot;Цифр:&quot;, digit_count)
print(&quot;Пробілів:&quot;, space_count)
Приклад 5. Перевірка паліндрома після нормалізації
text = input(&quot;Текст: &quot;)
normalized = text.lower().replace(&quot; &quot;, &quot;&quot;)
if normalized == normalized[::-1]:
print(&quot;Паліндром&quot;)
else:
print(&quot;Не паліндром&quot;)
Приклад 6. split() та join()
sentence = input(&quot;Речення: &quot;)
words = sentence.split()
print(words)
print(&quot;-&quot;.join(words))
Приклад 7. Пошук найдовшого слова
sentence = input(&quot;Речення: &quot;)
words = sentence.split()
longest = words[0]
for word in words:
if len(word) &gt; len(longest):
longest = word
print(&quot;Найдовше слово:&quot;, longest)
Приклад 8. replace() та очищення тексту
text = &quot; Python, Python, Python! &quot;
text = text.strip()
text = text.replace(&quot;Python&quot;, &quot;JavaScript&quot;)
print(text)
Приклад 9. Перевірка простого ідентифікатора
code = input(&quot;Код: &quot;)
if code.isalnum() and code[0].isalpha():
print(&quot;Формат коректний&quot;)
else:
print(&quot;Некоректний формат&quot;)
Приклад 10. Анаграми
text1 = input(&quot;Перший рядок: &quot;)
text2 = input(&quot;Другий рядок: &quot;)
a = text1.lower().replace(&quot; &quot;, &quot;&quot;)

Сторінка 5

b = text2.lower().replace(&quot; &quot;, &quot;&quot;)
if sorted(a) == sorted(b):
print(&quot;Анаграми&quot;)
else:
print(&quot;Не анаграми&quot;)
Приклад 11. Простий зсув символів
text = input(&quot;Текст: &quot;)
result = &quot;&quot;
for char in text:
result += chr(ord(char) + 1)
print(&quot;Результат:&quot;, result)
