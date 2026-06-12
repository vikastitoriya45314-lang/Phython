
students = {
    "Rahul": {"age": 20, "marks": 85},
    "Priya": {"age": 19, "marks": 90},
    "Amit": {"age": 21, "marks": 78}
}

students["Sneha"] = {"age": 20, "marks": 92}
students["Rahul"]["marks"] = 95

del students["Amit"]

print("Priya exists:", "Priya" in students)

print("\nKeys:")
for key in students.keys():
    print(key)
print("\nValues:")
for value in students.values():
    print(value)
print("\nItems:")
for item in students.items():
    print(item)
name_list = list(students.keys())
print("\nStudent Names List:", name_list)