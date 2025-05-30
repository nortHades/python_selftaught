# Create a student grade management system that:
# 1. Stores student names in a list
# 2. Stores their grades in separate lists (Math, English, Science)
# 3. Calculate average grade for each student
# 4. Find the student with highest average
# 5. Create a tuple containing (name, average) for each student
# 6. Sort students by their average grade (highest first)
# 7. Use string methods to format a nice report
student_name = ["John", "Sarah", "Cutti", "Choy"]
math_grade = [95, 74, 85, 80]
english_grade = [66, 86, 86, 90]
science_grade = [90, 80, 90, 85]
avg_grade = []
for i in range(len(student_name)):
    avg = (math_grade[i] + english_grade[i] + science_grade[i]) / 3
    avg_grade.append((student_name[i], round(avg, 2)))

max = ["", 0]
for i in range(len(avg_grade)):
    if avg_grade[i][1] > max[1]:
        max = avg_grade[i]
print(f"The students with highest avg grade is: {max[0]}")

avg_grade.sort(key=lambda x: x[1], reverse=True)
print(avg_grade)
print("\n" + "="*50)
print("📊 STUDENT GRADE REPORT".center(50))
print("="*50)

for i, (name, avg) in enumerate(avg_grade, 1):
    student_index = student_name.index(name)
    
    print(f"#{i} {name.upper():.<15} Average: {avg:>6.2f}")
    print(f"    Math: {math_grade[student_index]:>3} | English: {english_grade[student_index]:>3} | Science: {science_grade[student_index]:>3}")
    print("-" * 50)

print(f"\n🏆 TOP PERFORMER: {max[0]} with {max[1]:.2f} average")
print("="*50)