def task1():
    print("--- Завдання 1 ---")
    with open("text.txt", "r", encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file]

    num_lines = len(lines)
    full_text = "\n".join(lines)
    num_words = len(full_text.split())
    num_chars = sum(len(line) for line in lines)

    longest_idx = 0
    longest_line = ""
    for i, line in enumerate(lines, start=1):
        if len(line) > len(longest_line):
            longest_line = line
            longest_idx = i

    print(f"Рядків: {num_lines}")
    print(f"Слів: {num_words}")
    print(f"Символів: {num_chars}")
    print(f"Найдовший рядок: №{longest_idx}, {len(longest_line)} символів")
    print(f"Текст: {longest_line}\n")




def task2():
    print("--- Завдання 2 ---")
    query = input("Введіть фрагмент для пошуку: ").strip().lower()
    found = False

    with open("text.txt", "r", encoding="utf-8") as file:
        for i, line in enumerate(file, start=1):
            clean_line = line.rstrip("\n")
            if query in clean_line.lower():
                print(f"{i}: {clean_line}")
                found = True

    if not found:
        print("Збігів не знайдено.")
    print()




def task3():
    print("--- Завдання 3 ---")
    passed_students = []

    with open("students.txt", "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue
            name, score_str = clean_line.split(";")
            score = int(score_str)
            if score > 80:
                passed_students.append((name, score))

    passed_students.sort(key=lambda item: item[1], reverse=True)

    with open("result.txt", "w", encoding="utf-8") as out_file:
        for name, score in passed_students:
            out_file.write(f"{name};{score}\n")

    print("Файл result.txt успішно сформовано.\n")




def load_grades(filename):
    students_grades = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue
            name, subject, grade_str = clean_line.split(";")
            grade = float(grade_str)
            if name not in students_grades:
                students_grades[name] = []
            students_grades[name].append(grade)
    return students_grades
def calculate_stats(students_grades):
    stats = []
    for name, grades in students_grades.items():
        count = len(grades)
        avg = sum(grades) / count
        stats.append({"name": name, "count": count, "avg": avg})
    stats.sort(key=lambda x: x["avg"], reverse=True)
    return stats
def write_report(filename, stats):
    with open(filename, "w", encoding="utf-8") as out_file:
        for st in stats:
            out_file.write(
                f"{st['name']} — оцінок: {st['count']} — середній: {st['avg']:.2f}\n"
            )
        if stats:
            max_avg = stats[0]["avg"]
            best_students = [
                st["name"] for st in stats if round(st["avg"], 2) == round(max_avg, 2)
            ]
            best_names_str = " та ".join(best_students)
            out_file.write(f"Найкращий результат: {best_names_str} — {max_avg:.2f}\n")
def task4():
    print("--- Завдання 4 ---")
    grades_data = load_grades("grades.csv")
    stats = calculate_stats(grades_data)
    write_report("report.txt", stats)
    print("Файл report.txt успішно сформовано.\n")


if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
