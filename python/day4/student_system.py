students = {}
input_int = int(input("input:\n"))


def student_system_main(operate_nums):
    operate_orders = []
    for i in range(operate_nums):
        operate_orders.append(input())

    operate_fuc(operate_orders)


def operate_fuc(operate_orders):
    for order in operate_orders:
        order_clean = []
        order_word = order.strip().split()
        order_clean = list(w.strip(",.?!").lower() for w in order_word)
        if not order_clean:
            continue
        if order_clean[0] == "add":
            stat_add(order_clean[1], order_clean[2])
        elif order_clean[0] == "stats":
            stat_display()
        elif order_clean[0] == "filter":
            stat_filter(order_clean[1], order_clean[2])


def stat_add(name, grade):
    # validation
    global students
    students[name] = float(grade)


def stat_display():
    if not students:
        return
    avg = sum(students.values()) / len(students)
    maxium_student = max(students, key=lambda student: students[student])
    minmum_studnet = min(students, key=lambda student: students[student])
    passed_student = len(list(s for s in students if students[s] >= 60))
    print(f"The average scores: {avg:.2f}")
    print(f"Student name: {maxium_student}, highest score: {students[maxium_student]}")
    print(f"Student name: {minmum_studnet}, highest score: {students[minmum_studnet]}")
    print(f"Passed people count: {passed_student}")


def stat_filter(condition, grade):
    global students
    filter_students = {}
    grade_num = float(grade)
    if condition == "above":
        filter_students = dict(filter(lambda x: students[x] > grade_num, students))
    elif condition == "below":
        filter_students = dict(filter(lambda x: students[x] < grade_num, students))
    elif condition == "equal":
        filter_students = dict(filter(lambda x: students[x] == grade_num, students))

    if not filter_students:
        return
    for name, score in filter_students.items():
        print(f"{name}: {score}")


student_system_main(input_int)
