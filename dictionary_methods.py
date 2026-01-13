# Dictionary Methods & Nested Dictionaries

# Basic dictionary
student = {"name": "Saif", "age": 20}

# get() method
print(student.get("name"))
print(student.get("marks", "Not Found"))

# update() method
student.update({"age": 21, "city": "Delhi"})
print(student)

# popitem() method
student.popitem()
print(student)

# copy dictionary
student_copy = student.copy()
print(student_copy)

# Nested dictionary
students = {
    1: {"name": "Saif", "age": 20},
    2: {"name": "Rahul", "age": 21}
}

print(students[1]["name"])

# Looping through nested dictionary
for roll, info in students.items():
    print("Roll:", roll)
    for key, value in info.items():
        print(key, ":", value)

# Dictionary with list values
marks = {
    "Saif": [80, 85, 90],
    "Rahul": [70, 75, 78]
}

print(marks["Saif"])

# Real-life user profile
user = {
    "username": "saif123",
    "email": "saif@gmail.com",
    "skills": ["Python", "SQL", "Backend"]
}

print(user)
