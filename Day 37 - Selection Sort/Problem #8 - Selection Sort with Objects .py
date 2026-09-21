students = [
    {"name": "Ali", "marks": 78},
    {"name": "Ahmed", "marks": 92},
    {"name": "Usman", "marks": 65},
    {"name": "Bilal", "marks": 85}
]

for i in range(len(students)-1):
    largest=i
    for j in range(i+1 , len(students)):
        if students[j]["marks"] > students[largest]["marks"]:
            largest=j

    students[i] , students[largest] = students[largest] , students[i]

print(students)