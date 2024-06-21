# Nesting
age = int(input("\nPlease Enter Your Age: "))

if (age >= 18):
    if (age >= 80):
        print("\nSorry, You Cannot Drive.")
    else:
        print("\nYou Can Drive.")
else:
    print("\nSorry, You Cannot Drive.")