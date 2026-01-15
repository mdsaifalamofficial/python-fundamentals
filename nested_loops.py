# Nested Loops in Python

# Simple nested loop
for i in range(3):
    for j in range(2):
        print("i =", i, "j =", j)

print()

# Nested loop with while
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(i, j)
        j += 1
    i += 1

print()

# Square star pattern
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

print()

# Right-angle triangle pattern
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()

print()

# Number pattern
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()

# Reverse star pattern
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
