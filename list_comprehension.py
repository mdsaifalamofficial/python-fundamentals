# List Comprehension in Python

# Basic list comprehension
numbers = [i for i in range(1, 6)]
print(numbers)

# With condition (even numbers)
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

# Using existing list
nums = [1, 2, 3, 4, 5]
squares = [x * x for x in nums]
print(squares)

# With string
word = "Python"
letters = [ch for ch in word]
print(letters)

# if-else in list comprehension
result = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 6)]
print(result)

# Nested list comprehension (intro)
pairs = [(i, j) for i in range(1, 3) for j in range(1, 3)]
print(pairs)
