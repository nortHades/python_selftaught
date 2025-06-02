empty_set = set()  # {} create dict not set

# set with initial values
numbers = {1, 2, 3, 4, 5}
colors = set(["red", "green", "blue"])
# From string
letters = set("hello")

# Add and remove elements
numbers.add(6)
numbers.remove(1)  # Raises KeyError if not found
numbers.discard(10)  # No error if not found

# set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2  # {1,2,3,4,5,6}
intersection = set1 & set2  # {3,4}
difference = set1 - set2  # {1,2}
symmetric_diff = set1 ^ set2  # {1,2,5,6}

# check relationships
is_subset = {1, 2}.issubset(set1)  # true
is_superset = set1.issuperset({1, 2})  # true
is_disjoint = set1.isdisjoint({7, 8})  # true
