import os
with open("employees.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Priya\n")
    file.write("Amit\n")
print("Original File:")
with open("employees.txt", "r") as file:
    print(file.read())
with open("employees.txt", "a") as file:
    file.write("Sneha\n")
    file.write("Rohan\n")
print("Updated File:")
with open("employees.txt", "r") as file:
    print(file.read())
os.remove("employees.txt")
if os.path.exists("employees.txt"):
    print("File still exists")
else:
    print("File deleted successfully")