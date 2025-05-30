# Create strings
message = "Hello, world!"
name = "Python"
multiline = """
This is a 
multi-line string
"""
# Indexing and slicing (same as list/tuples)
print(message[0])
print(message[-1])
print(message[7:12])
print(message[:5])
print(message[::2])

# Common string methods
text = "  Python Programming  "
print(text)
print(text.strip())  # "Python Programming" (remove whitespace)
print(text.lower())
print(text.upper())
print(text.replace("Python", "Java"))
print(text)  # nochange to the original one
print(text.split())  # ['Python', 'Programming']

# string formatting
age = 25
formatted = f"I am {age} years old"
formatted2 = "I am {} years old".format(age)

# string checking methods
word = "hello123_"
print(word.isalnum())  # true alpha-numeric
print(word.isalpha())  # false, all should be alpha
print(word.isdigit())  # false
print(word.startswith("hel"))  # true
print(word.endswith("23_"))  # true
