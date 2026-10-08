n = int(input("Введіть N: "))
s = 0
k = 0
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        s += i
        k += 1
print("Кількість:", k)
print("Сума:", s)
if k > 0:
    print("Середнє:", s / k)




n = int(input("Введіть N: "))
if n == 0:
    print("Кількість цифр: 1")
    print("Сума цифр: 0")
    print("Найбільша цифра: 0")
    print("Найменша цифра: 0")
else:
    k = 0
    s = 0
    mx = 0
    mn = 9
    while n > 0:
        d = n % 10
        k += 1
        s += d
        if d > mx:
            mx = d
        if d < mn:
            mn = d
        n = n // 10
    print("Кількість цифр:", k)
    print("Сума цифр:", s)
    print("Найбільша цифра:", mx)
    print("Найменша цифра:", mn)

n = int(input("Введіть N: "))





for i in range(1, n + 1):
    t = i
    ok = True

    while t > 0:
        d = t % 10
        if d != 0 and i % d != 0:
            ok = False
            break
        t = t // 10

    if ok:
        print(i, end=" ")
print()



w = int(input("width = "))
h = int(input("height = "))
a = input("контур = ")
b = input("всередині = ")

if w < 3 or h < 3:
    print("Помилка! Мінімальний розмір 3х3")
else:
    for r in range(h):
        for c in range(w):
            if r == 0 or r == h - 1 or c == 0 or c == w - 1:
                print(a, end="")
            else:
                print(b, end="")
        print()



h = int(input("Введіть висоту трикутника: "))
s = input("Введіть символ: ")
if h < 1:
    print("Помилка! Висота повинна бути більше 0")
else:
    for r in range(1, h + 1):
        for c in range(r):
            print(s, end="")
        print()
