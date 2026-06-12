students = ["Rahul", "Priya", "Amit", "Sneha", "Rohan"]
students.append("Vikas")     
students.insert(2, "Anjali")  

print("After adding names:", students)
students.remove("Amit")

print("After removing names:", students)
students.sort()

print("Reverse sorted list:", students[::-1])
print("First 3 elements:", students[:3])

