def area_circle(radius, pi=3.14159):
    return pi * (radius ** 2)
def area_rectangle(a, b):
    return a * b
def area_triangle(base, height):
    return 0.5 * base * height
def main():
    shape = input("Фігура: ").strip().lower()
    if shape == "прямокутник":
        w = int(input("Ширина: "))
        h = int(input("Висота: "))
        res = area_rectangle(w, h)
        print(f"Площа прямокутника: {res}")
    elif shape == "круг":
        r = float(input("Радіус: "))
        res = area_circle(r)
        print(f"Площа круга: {res}")
    elif shape == "трикутник":
        b = float(input("Основа: "))
        h = float(input("Висота: "))
        res = area_triangle(b, h)
        print(f"Площа трикутника: {res}")
    else:
        print("Невідома фігура")
if __name__ == "__main__":
    main()




def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def divisors(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
def main():
    n = int(input("N = "))
    prime_str = "так" if is_prime(n) else "ні"
    divs = divisors(n)
    d_sum = digit_sum(n)
    print(f"Просте число: {prime_str}")
    print(f"Дільники: {divs}")
    print(f"Сума цифр: {d_sum}")
if __name__ == "__main__":
    main()



def average(grades):
    if not grades:
        return 0.0
    return sum(grades) / len(grades)
def minimum(grades):
    return min(grades)
def maximum(grades):
    return max(grades)
def count_above(grades, value):
    count = 0
    for grade in grades:
        if grade > value:
            count += 1
    return count
def main():
    grades = [10, 8, 12, 9, 11]
    limit = 9
    avg_val = average(grades)
    min_val = minimum(grades)
    max_val = maximum(grades)
    above_val = count_above(grades, limit)
    print(f"Середній бал: {avg_val:.1f}")
    print(f"Мінімальна: {min_val}")
    print(f"Максимальна: {max_val}")
    print(f"Вище {limit}: {above_val}")
if __name__ == "__main__":
    main()


def check_len(password):
    return len(password) >= 8
def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False
def has_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False
def has_lower(password):
    for char in password:
        if char.islower():
            return True
    return False
def has_special(password):
    for char in password:
        if not char.isalnum():
            return True
    return False
def validate_password(password):
    errors = []
    if not check_len(password):
        errors.append("довжина менше 8 символів")
    if not has_digit(password):
        errors.append("немає цифри")
    if not has_upper(password):
        errors.append("немає великої літери")
    if not has_lower(password):
        errors.append("немає малої літери")
    if not has_special(password):
        errors.append("немає спеціального символу")
    return len(errors) == 0, errors
def main():
    pwd = input("Password: ")
    is_valid, errors = validate_password(pwd)
    if is_valid:
        print("Пароль надійний")
    else:
        print("Пароль не відповідає вимогам.")
        for err in errors:
            print(f"Не виконано: {err}")
if __name__ == "__main__":
    main()
