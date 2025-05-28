# range(stop) - from 0 to stop-1
for i in range(3):
    print(i)

# range(start, stop) - from start to stop
for i in range(2, 7):
    print(i)

# range(start, stop, step)
for i in range(2, 8, 2):
    print(i)

# reverse range(start, stop, step)
# start: bigger one
# stop: smaller one
# step: negative integer
for i in range(10, 0, -1):
    print(i)

# convert range to list
numbers = list(range(5))
print(numbers)  # [0,1,2,3,4]
