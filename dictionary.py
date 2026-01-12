# Dictionary in Python

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Delhi"
}

print(student)

# Access values
print(student["name"])
print(student["age"])

# Update value
student["age"] = 21

# Add new key-value
student["course"] = "Python"

# Remove value
student.pop("city")

print(student)

# Dictionary methods
print(student.keys())
print(student.values())
print(student.items())

# Looping
for key, value in student.items():
    print(key, ":", value)

# Check key existence
print("name" in student)
