INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

students = {}
best_average = 0
best_student = ""
# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))
with open(INPUT_FILE, 'r') as file:
    next(file)

# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
#   - приберіть символ переносу рядка (line.strip())
#   - розбийте рядок по комі (line.split(","))
#   - перетворіть оцінки на числа (int або float)
    for line in file:
        cleaned = line.strip()
        split_line = line.split(',')
        student = split_line[0]
        grades = [int(x) for x in split_line[1:]]
        average = int(sum(grades) / len(grades))
        grades.append(average)
        students[student] = grades
        if average > best_average:
            best_average = average
            best_student = student

# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)
avarage_marks_by_elective = []
math_marks = []
python_marks = []
english_marks = []

for st in students:
    math_mark = students[st][0]
    math_marks.append(math_mark)
    python_mark = students[st][1]
    python_marks.append(python_mark)
    english_mark = students[st][2]
    english_marks.append(english_mark)
math_aver = sum(math_marks) / len(math_marks)
python_aver = sum(python_marks) / len(python_marks)
english_aver = sum(english_marks) / len(english_marks)
avarage_marks_by_elective.append(round(math_aver, 1))
avarage_marks_by_elective.append(round(python_aver, 1))
avarage_marks_by_elective.append(round(english_aver, 1))
print(avarage_marks_by_elective)

# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
with open("result.txt", "w", encoding="utf-8") as file:
    file.write("Середній бал по класу:\n")
    file.write(f"math: {avarage_marks_by_elective[0]}\n")
    file.write(f"python: {avarage_marks_by_elective[1]}\n")
    file.write(f"english: {avarage_marks_by_elective[2]}\n")
    file.write(f"Найкращий студент: {best_student} ({round(best_average, 1)})")

    print("Середній бал по класу:")
    print(f"math: {avarage_marks_by_elective[0]}")
    print(f"python: {avarage_marks_by_elective[1]}")
    print(f"english: {avarage_marks_by_elective[2]}")
    print(f"Найкращий студент: {best_student} ({round(best_average, 1)})")



# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
