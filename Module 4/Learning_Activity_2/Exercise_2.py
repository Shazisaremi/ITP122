students = {"name": ['Luis', 'Maria', 'Jack'], "id": [1, 2, 3]}

print(students["name"][1])

print(students["id"][1])

students["name"].append("Sara")
students["id"].append(4)

print(students)

if 123 in students["id"]:
    print(True)
else:
    print(False)