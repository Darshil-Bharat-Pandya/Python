# Dictionary in Python

# Dictionaries are used to store data values in key:value pairs. They are unordered, mutable(changeable) and don't allow duplicate keys.

info = {
    "name" : "apnacollege",
    "subjects" : ["python", "C", "java"],
    "topics" : ("dict", "set"),
    "age" : 35,
    "is_adult" : True,
    12.99 : 94.4
}

info["name"] = "Darshil"
info["surname"] = "Pandya"
info["subjects"] = "Python, Machine Learning"
info["topics"] = "Decision Tree, Regression"
info["age"] = 22
info["is_adult"] = True
info[12.99] = 94.4

print(info)
print(type(info))

null_dict = {}
print(null_dict)
print(type(null_dict))