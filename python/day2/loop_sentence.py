# for loop - iterate through sequences
fruits = [
    "apple",
    "banana",
    "cherry",
]  # as habitat, single string using '', complex string using ""
for fruit in fruits:
    print(f"I like {fruit}")

# for loop with index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# while loop - continue until condition is false
counter = 0
while counter < 3:
    print(f"counter: {counter}")
    counter += 1
