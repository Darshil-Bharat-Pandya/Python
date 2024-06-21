# Practice Question

# WAP to count the number of students from the list who got the different grades and also store the above values in a list and store them from "A" to "D".

list1 = ["A1", "D4", "Fail", "A1", "B2", "Fail", "A1", "C3", "C3", "C3", "D4", "D4", "A1", "B2", "C3", "Fail", "Fail"]

print("\n", list1)

list2 = list1.count("A1")
list3 = list1.count("B2")
list4 = list1.count("C3")
list5 = list1.count("D4")
list6 = list1.count("Fail")

print("\nThe number of students who got A1 grade are", list2)
print("The number of students who got B2 grade are", list3)
print("The number of students who got C3 grade are", list4)
print("The number of students who got D4 grade are", list5)
print("The number of students who Failed are", list6)

list1.sort()
print("\n", list1)

print("\n")