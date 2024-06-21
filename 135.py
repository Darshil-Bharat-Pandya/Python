# Practice Question

# WAP to check that if a list contains a palindrome of elements. (Hint: use copy() method)

list = []

list.append(int(input("\nPlease Enter the First Value: ")))
list.append(int(input("Please Enter the Second Value: ")))
list.append(int(input("Please Enter the Third Value: ")))

print("\nYou Entered:", list)

copy_list = list.copy()
copy_list.reverse()

if (list == copy_list) :
    print("\nIt is a Palindrome.")
else :
    print("\nIt is not a Palindrome.")
    
print("\n")