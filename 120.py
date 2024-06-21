# Lists in Python

# It is a built-in data type that stores a set of values.
# It can store elements of different types (integer, float, string and etc.)

# marks = [87, 64, 33, 95, 76] = marks[0], marks[1]...
# student = ["karan", 85, "Delhi"] = student[0], student[1]...
# student[0] = "Arjun" = allowed in python
# len(student) = It returns the length.

# Strings are Immutable.
# Lists are Mutable.

marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print("\n",marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])
print(marks[-1])

student = ["karan", 95.4, 17, "Delhi"]
print("\n",student)
print(type(student))
print(len(student))
print(student[0])
print(student[1])
print(student[2])
print(student[-1])

print("\n",student[0])
student[0] = "arjun"
print(student)
print(student[3])
print(student[-1])