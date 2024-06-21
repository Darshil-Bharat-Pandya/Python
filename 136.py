# Practice Question

# WAP to count the number of students with the "A" grade in the following tuple. ["C", "D", "A", "A", "B", "B", "A"] and also store the above values in a list and sort them from "A" to "D".

list1 = ["C", "D", "A", "A", "B", "B", "A"]
print("\n", list1)

list2 = list1.count("A")
list3 = list1.count("B")
list4 = list1.count("C")
list5 = list1.count("D")

print("\nThe Number of Students who got A grade are", list2)
print("The Number of Students who got B grade are", list3)
print("The Number of Students who got C grade are", list3)
print("The Number of Students who got D grade are", list4)

list1.sort()
print("\n",list1)

print("\n")