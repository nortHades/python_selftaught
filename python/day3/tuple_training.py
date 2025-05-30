# Create tuples
fruits = ["grape", "apple", "banana"]
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (42,)
empty_tuple = ()

# Indexing and slicing (same as list)
print(coordinates)
print(colors[1:])
print(colors[::-1])

# Tuple unpacking
x, y = coordinates
first, *rest = colors

# Tuples are immutable

# Common tuple methods
print(colors.count("red"))
print(colors.index("blue"))

# Converting between tuples and lists
list_from_tuple = list(colors)
tuple_from_list = tuple(fruits)
