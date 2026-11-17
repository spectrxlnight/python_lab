import tkinter as tk
import student_utils
def make_report():
    val = entry.get().strip()
    if not val.isdecimal():
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, "Введіть ціле число від 1 до 20")
        return
    count = int(val)
    if count < 1 or count > 20:
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, "Число повинно бути від 1 до 20")
        return
    students = ["Anna", "Ivan", "Olha"]
    report = ""
    for name in students:
        grades = student_utils.generate_grades(count)
        avg = student_utils.average_grade(grades)
        lvl = student_utils.get_level(avg)
        line = f"{name}: {grades} -> {avg} -> {lvl}\n"
        report += line
    print(report)
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, report)
window = tk.Tk()
window.title("Статистика учнів")
window.geometry("500x300")
tk.Label(window, text="Кількість оцінок (1-20):").pack(pady=5)
entry = tk.Entry(window)
entry.pack(pady=5)
tk.Button(window, text="Сформувати звіт", command=make_report).pack(pady=10)
text_box = tk.Text(window, width=55, height=10)
text_box.pack(pady=5)
window.mainloop()
