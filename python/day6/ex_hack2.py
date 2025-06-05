flag = True
a_list = input().strip().split()
a_set = set(a_list)
num_of_others = int(input())
for _ in range(num_of_others):
    child_set = set(input().strip().split())
    if not (a_set > child_set):
        flag = False
        break

print(flag)
