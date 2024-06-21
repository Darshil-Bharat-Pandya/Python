# Dictionary Methods

# myDict.keys() = It returns all the keys.
# myDict.values() = It returns all the values.
# myDict.items() = It returns all (key, val) pairs as tuples.
# # myDict.get("key") = It returns all the key according to value.
# # myDict.update(newDict) = It inserts the specified items to the dictionaries.

student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(len(student))
print(list(student.keys()))
print(len(list(student.keys())))

College = {
    "Name" : "IIT-Delhi",
    "Ranking" : "All India Rank-3 in terms of Engineering.",
    "Departments" : {
        "CSE" : 2341,
        "Electrical" : 2342,
        "Mechanical" : 2343,
        "Civil" : 2344
    }
}

print(type(College))
print(College)
print(len(College))
print(College.keys())
print(len(College.keys()))
print(len(list(College.keys())))