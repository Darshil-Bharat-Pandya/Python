# Practice Question.

# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 81, 100)

num = (1, 4, 9, 16, 25, 36, 64, 81, 100)

x = int(input("Please Enter the value of x: "))

i = 0
while (i < len(num)):
    if(num[i] == x):
        print("Found at idx", i)
    else:
        print("Finding...")
    i += 1