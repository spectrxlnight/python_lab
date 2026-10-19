s=input("Введіть рядок: ")
l = len(s)  
a = sum(1 for c in s if c.isalpha())  
d = sum(1 for c in s if c.isdigit())  
p = sum(1 for c in s if c.isspace())  
v = sum(1 for c in s.lower() if c in "aeiouyаеєиіїоуюя")  
w = len(s.split())  
print(f"Символів: {l}")
print(f"Літер: {a}")
print(f"Цифр: {d}")
print(f"Пробілів: {p}")
print(f"Голосних: {v}")
print(f"Слів: {w}")


s=input("ПІБ: ")
p = s.split()
if len(p) == 3:
    f = p[0].capitalize()
    i = p[1].capitalize()
    o = p[2].capitalize()
    res = f"{f} {i[0]}. {o[0]}"
    print(res)
else:
    print("Три слова не введено")



a = input("Введіть перший рядок: ")
b = input("Введіть другий рядок: ")
x = "".join(sorted(c.lower() for c in a if c.isalpha()))
y = "".join(sorted(c.lower() for c in b if c.isalpha()))
if x == y:
    print(f"Рядки є анаграмами: '{x}' та '{y}'")
else:
    print(f"Рядки не є анаграмами: '{x}' та '{y}'")




s = input("Введіть речення: ")
w = s.split()
mn = len(w[0])
mx = len(w[0])
for x in w:
    if len(x) < mn:
        mn = len(x)
    if len(x) > mx:
        mx = len(x)
a = []  
b = []  
for x in w:
    if len(x) == mn and x not in a:
        a.append(x)
    if len(x) == mx and x not in b:
        b.append(x)
u = []
for x in w:
    t = x.lower()
    if t not in u:
        u.append(t)
o = input("Що: ")
n = input("На що: ")
r = s.replace(o, n)
print(f"Найдовші: {', '.join(b)}")
print(f"Найкоротші: {', '.join(a)}")
print(f"Унікальних слів: {len(u)}")
print(f"Після заміни: {r}")
