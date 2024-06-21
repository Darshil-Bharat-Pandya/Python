# WAP to check that, if a list contains a palindrome of elements. (Hint: use copy() method.)

list = []

list.append(int(input("\nEnter the First Value: ")))
list.append(int(input("Enter the Second Value: ")))
list.append(int(input("Enter the Third Value: ")))

print("\n",list)

copy_list = list.copy()
copy_list.reverse()

if ( list == copy_list):
    print("\nIt is a Palindrome.")
else:
    print("\nIt is not a Palindrome.")
    
print("\n")