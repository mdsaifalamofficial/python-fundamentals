# Sets in Python (Unique Elements)

numbers = {1, 2, 2, 3, 4}
print(numbers)

# Empty set
s = set()
print(s)

# Add elements
numbers.add(5)
print(numbers)

# Update multiple elements
numbers.update([6, 7])
print(numbers)

# Remove elements
numbers.remove(3)
print(numbers)

numbers.discard(10)   # no error
print(numbers)

# Pop random element
numbers.pop()
print(numbers)

# Membership check
print(2 in numbers)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union
print(a & b)   # Intersection
print(a - b)   # Difference
