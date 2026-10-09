students = [
    {"name": "Ravi", "marks": 85},
    {"name": "Sita", "marks": 92},
    {"name": "Raju", "marks": 67},
    {"name": "Priya", "marks": 78},
    {"name": "Anu", "marks": 95}
]

total = 0

print("STUDENT PERFORMANCE ANALYSIS")
print("----------------------------")

for student in students:
    name = student["name"]
    marks = student["marks"]
    total += marks

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"

    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)
    print("----------------------------")

average = total / len(students)
topper = max(students, key=lambda s: s["marks"])

print("Total Students:", len(students))
print("Average Marks:", round(average, 2))
print("Topper:", topper["name"])
print("Highest Marks:", topper["marks"])
