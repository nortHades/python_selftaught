n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
query_scores = []
if query_name in student_marks:
    query_scores = student_marks[query_name]
if query_scores:
    avg = sum(query_scores) / len(query_scores)
print(avg)
