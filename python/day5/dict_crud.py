# empty dictionary
empty_dict = {}
empty_dict = dict()

# Dictionary with initial values
student = {"name": "Alice", "age": 20, "grade": "A"}
coordinates = dict(x=10, y=20)

# from the lists of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)

# Access values
print(student["name"])
print(student.get("age"))
print(student.get("height", 0))

# modify values
student["age"] = 21
student["major"] = "Computer Science"

# Delete items
del student["grade"]
removed_value = student.pop("major", "Not found")


# regular methods for dicts
keys = student.keys()
values = student.values()
items = student.items()

if "name" in student:
    print("Name exists")

# update
# if existing, upadate the value, if not, upadate the key
student.update({"city": "Beijing", "age": 22})

# clear dicitonary
student.clear()
