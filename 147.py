student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

new_dict = {"name" : "neha kumar", "age" : 16}
student.update(new_dict)

print(student)