# Strings in Python

# Creating strings
name = "Saif"
city = 'Delhi'
print(name)
print(city)

# Indexing
word = "Python"
print(word[0])
print(word[3])

# Length
print(len(word))

# Looping through string
for ch in word:
    print(ch)

# String immutability
# name[0] = "R"  # This will cause error

# String methods
text = "python"
print(text.upper())
print("PYTHON".lower())
print("python programming".title())
print("python".capitalize())

# strip()
msg = "  hello  "
print(msg.strip())

# replace()
lang = "I like Java"
print(lang.replace("Java", "Python"))

# find()
print("Python".find("t"))

# count()
print("banana".count("a"))

# Checking content
print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())

# split() and join()
sentence = "I love Python"
words = sentence.split()
print(words)

new_sentence = " ".join(words)
print(new_sentence)

# Concatenation
a = "Hello"
b = "World"
print(a + " " + b)

# Formatting (basic)
age = 20
print("My name is", name, "and my age is", age)
