# Regular function
def square(x):
    return x**2


# Equivalent Lambda function
square_lambda = lambda x: x**2

print(square(5))
print(square_lambda(5))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Using Lambda with map()
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# using Lambda with sorted()
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
sorted_by_grade = sorted(students, key=lambda student: student[1])
print(sorted_by_grade)

# Good for simple, one-line functions
operations = {
    "add": lambda x, y: x + y,
    "multiply": lambda x, y: x * y,
    "power": lambda x, y: x**y,
}

result = operations["add"](5, 3)  # Result: 8


# Complex logic should use regular functions, not lambda
def complex_calculation(data):
    processed = []
    for item in data:
        if item > 0:
            processed.append(item**2)
        else:
            processed.append(abs(item))
    return sum(processed)
