def input_record():
    records = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # store the data in dict
        records[name] = score

    sorted_records = sorted(list(set(records.values())))
    print(sorted_records)
    # get the second lowest grade
    second_grade = -1
    if len(sorted_records) > 1:
        second_grade = sorted_records[1]

    # get names list of 2nd lowest grade
    name_list = []
    for key, value in records.items():
        if value == second_grade:
            name_list.append(key)
    print(sorted(name_list))


input_record()
