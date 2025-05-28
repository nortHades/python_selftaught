# Control Flow Keywords
# break - exit the loop completely
for i in range(10):
    if i == 5:
        print("breaking at 5")
        break
    print(i)  # 5 wont be printed

# continue - skip current iteration, go to next
for i in range(10):
    if i == 5:
        print("skipping 5")
        continue
    print(i)

# else clause with loops (executes if loop completes normally)
for i in range(3):
    print(i)
else:
    print("loop completed normally")
# when the loop be executed without break, the else will be executed
for i in range(3):
    if i == 2:
        print("breaking at 2")
        break
    print(i)
else:
    print("loop completed normally")
