# Tuples in Python (Immutable Data Structure)

numbers = (1, 2, 3, 4)
names = ("Saif", "Rahul", "Aman")

print(numbers)
print(names)

# Single-item tuple
single = (10,)
print(single)

# Indexing
print(names[0])
print(names[1])

# Looping through tuple
for name in names:
    print(name)

# Tuple methods
t = (1, 2, 2, 3)
print(t.count(2))
print(t.index(3))
