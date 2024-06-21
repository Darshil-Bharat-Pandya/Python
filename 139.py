# Dictionary in Python

# Dictionaries are used to store data values in key:value pairs. They are unordered, mutable(changeable) and they don't allow keys.

# Example =
# dict = {
#       "name" : "shradha",
#       "cgpa" : 9.6,    
#       "marks" : [98, 97, 95],
#        }

# dict["name"], dict["cgpa"], dict["marks"]
# dict["key"] = "value" // to assign or add new.

info = {
    "name" : "apnacollege",
    "subjects" : ["Python", "C", "Java"],
    "topics" : ("dict", "set"),
    "age" : 35,
    "is_adult" : True,
    12.99 : 94.4
}

print(type(info))

print(info["name"])
print(info["subjects"])
print(info["topics"])
print(info["age"])
print(info["is_adult"])
print(info[12.99])

info["name"] = 23
info["surname"] = "Pandya"
info["subjects"] = "Python","Machine Learning"
info["topics"] = "Decision Tree"
info["age"] = 22
info["is_adult"] = True

print(info)

null_dict = {}
null_dict["name"] = "apnacollege"
print(null_dict)