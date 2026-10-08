Приклад 1. Виведення 1..N циклом for
n = int(input('N = '))
for i in range(1, n + 1):
print(i)
Приклад 2. Те саме циклом while
n = int(input('N = '))
i = 1
while i <= n:
print(i)
i += 1
Приклад 3. Сума і середнє чисел 1..N
n = int(input('N = '))
total = 0
for i in range(1, n + 1):
total += i
print('Сума:', total)
print('Середнє:', total / n)
Приклад 4. Факторіал
n = int(input('N = '))
result = 1
for i in range(1, n + 1):
result *= i
print('Факторіал:', result)
Приклад 5. Сума чисел за умовою
n = int(input('N = '))
total = 0
for i in range(1, n + 1):
if i % 3 == 0:
total += i
print('Сума:', total)
