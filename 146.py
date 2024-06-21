student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

# student.update({"city" : "Ahmedabad"})
# It can also be executed by the below line of code.
new_city = ({"city" : "Ahmedabad"})
student.update(new_city)
student.update({"name" : "Darshil"})
student.update({"is_adult" : True})
print("\n",student)