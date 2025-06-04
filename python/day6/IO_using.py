# with sentence will close the files automatically
import datetime


with open("input.txt", "r") as file:
    content = file.read()
print(content)

# Read line by line
with open("input.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read all lines into list
with open("input.txt", "r") as file:
    lines = file.readlines()

# Write to file
with open("output.txt", "w") as file:
    file.write("Hello Python!\n")
    file.write("File operations are easy.")

