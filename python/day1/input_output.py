print("=== Input and Output Functions ===")

# print() function variations
print("Hello World")                    # Basic print
print("Hello", "World", "!")            # Multiple arguments
print("Name:", "Alice", "Age:", 25)     # Mixed types

# print() with separators and end characters
print("A", "B", "C", sep="-")          # Custom separator: A-B-C
print("Loading", end="...")            # Custom end character
print(" Done!")                        # Continues on same line with blankspace

# print() formatting
name = "Bob"
score = 95.5
print(f"Student: {name}, Score: {score}")           # f-string (modern)
print("Student: {}, Score: {}".format(name, score)) # .format() method
print("Student: %s, Score: %.1f" % (name, score)) # % format(old)

# input() function
print("\n=== Input Function Demo ===")
print("Let's collect some information:")

user_name = input("What's your name? ")
user_age = input("How old are you? ")

print(f"Hello {user_name}!")
print(f"You are {user_age} years old.")

# For demonstration without user interaction:
# Note: input() always returns string!

# Converting input to numbers
print(f"user_age type: {type(user_age)}")  # <class 'str'>
age_number = int(user_age)
print(f"age_number type: {type(age_number)}") # <class 'int'>