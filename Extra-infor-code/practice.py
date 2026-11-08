# DEBUG PRACTICE - Combined program: Student Result Manager
# Topics mixed: variables, conditions, list, tuple, dictionary, set, loops
# Is program mein 7 bugs hain (syntax, runtime aur logic teeno type).
# -------------------------------------------------------------------
# Expected output (sab fix hone ke baad):
# Student: Md | Subjects: 4
# Subject-wise marks:
# python: 88
# dsa: 72
# maths: 65
# physics: 35
# Total: 260 | Average: 65.0
# Result: PASS
# Failed subjects: ['physics']
# Unique grades: ['A', 'B', 'F']

student_name = "Md"
marks = {"python": 88, "dsa": 72, "maths": 65, "physics": 35}
subjects = tuple(marks.keys())
print("Student:", student_name, "| Subjects:", len(subjects))

print("Subject-wise marks:")
for subject in marks:
    print(subject + ":", marks[subject])

for subject, score in marks.items():
    total = 0
    total += score
average = total / len(marks)
print("Total:", total, "| Average:", average)

if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")

failed = []
for subject, score in marks.items():
    if score < 40:
        failed.append(subject)
print("Failed subjects:", failed)

grades = []
for score in marks.values():
    if score >= 75:
        grades.append("A")
    elif score >= 60:
        grades.append("B")
    elif score >= 40:
        grades.append("C")
    else:
        grades.append("F")
print("Unique grades:", sorted(set(grades)))