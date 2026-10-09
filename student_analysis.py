```python
import csv

students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["Marks"] = int(row["Marks"])
        row["Attendance"] = int(row["Attendance"])
        students.append(row)

print("STUDENT PERFORMANCE ANALYSIS")
print("----------------------------")

total_marks = 0

for student in students:
    marks = student["Marks"]
    total_marks += marks

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"

    print("Name:", student["Name"])
    print("Marks:", marks)
    print("Attendance:", student["Attendance"], "%")
    print("Grade:", grade)
    print("----------------------------")

average = total_marks / len(students)
topper = max(students, key=lambda s: s["Marks"])

print("Total Students:", len(students))
print("Average Marks:", round(average, 2))
print("Topper:", topper["Name"])
print("Highest Marks:", topper["Marks"])
