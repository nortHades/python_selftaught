# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]
empty_list = []

# Indexing (0-based)
print(fruits[0])  # 'apple'
print(fruits[-1])  # 'cherry' (last item)
print(fruits[-2])  # 'banana' (second from end)

# Slicing [start:end:step]
print(numbers[1:4])  # [2, 3, 4] (index 1 to 3)
print(numbers[:3])  # [1, 2, 3] (first 3 items)
# [3, 4, 5] (from index 2 to end)
print(numbers[2:])
# [1, 3, 5] (every 2nd item)
print(numbers[::2])
# reverse
print(numbers[::-1])

# Common list methods
fruits.append("orange")  # Add to end
fruits.insert(1, "grape")  # Insert at index 1
fruits.remove("banana")  # Remove first occurrence
popped = fruits.pop()  # Remove and return last item
fruits.extend(["kiwi", "mango"])  # Add multiple items
fruits.sort()  # Sort in place
fruits.reverse()  # Reverse in place

# List comprehensions (bonus)
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in numbers if x % 2 == 0]
