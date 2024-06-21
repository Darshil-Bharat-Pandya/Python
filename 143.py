Student = {
    "Name" : "Darshil",
    "Surname" : "Pandya",
    "Department" : "CSE",
    "Subjects" : {
        "Python" : 75,
        "C" :82,
        "Java" : 88,
        "C++" : 50
    } 
}

print(type(Student))
print(Student)
print(Student["Name"])
print(Student["Surname"])
print(Student["Department"])
print(Student["Subjects"])
print(Student["Subjects"]["Python"])
print(Student["Subjects"]["C"])
print(Student["Subjects"]["Java"])
print(Student["Subjects"]["C++"])