s1 = {"Python", "Java", "C++", "Python", "Java"}
print("Unique Set:", s1)

s2 = {"Python", "C", "JavaScript"}

print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference:", s1 - s2)

# Tuple
cities = ("Bhopal", "Indore", "Delhi", "Mumbai", "Bhopal")

print("Count of Bhopal:", cities.count("Bhopal"))
print("Index of Delhi:", cities.index("Delhi"))
print("Mumbai exists:", "Mumbai" in cities)

try:
    cities[0] = "Pune"
except TypeError:
    print("Error: Tuple cannot be modified")