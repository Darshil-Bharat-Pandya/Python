student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print("\n",len(student))

print("\n",list(student.keys()))

print("\n",len(list(student.keys())))

print("\n",student.values())

print("\n",list(student.values()))

pairs = list(student.items())
print("\n", pairs)
print("\n", pairs[0])
print("\n", pairs[1])

# print("\n", student["name2"]) = This Line of Code will show the Error.
print("\n", student.get("name2")) # = This Line of Code will not show the Error.

d = {"coding" : "good", "thinking" : "better"}
print("\n",d.get("coding"))

b = {1: "001", 2: "010", 3: "011"}
# Since 4 is not in keys, it will print "Not Found"
print("\n", b.get(4, "Not Found"))

print("\n")

# The Python Dictionary get() Method returns the value for the given key if present in the dictionary. If not, then it will return None(if get() is used with only argument).