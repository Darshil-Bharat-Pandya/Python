# WAP to check that, if a list contains a palindrome of elements. (Hint: use copy() method.)

list = [1, 2, 3, 4, 5]

copy_list = list.copy()
copy_list.reverse()

if (copy_list == list):
    print("\nIt is a Palindrome.")
else:
    print("\nIt is not a Palindrome.")
    
print("\n")