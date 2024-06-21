# Rules for AND and OR Table.

# AND
# True AND True = True
# False AND True = False
# True AND False = False
# False AND False = False

# OR
# True OR True = True
# False OR True = True
# True OR False = True
# False OR False = False

# Practice Question
# Print output for:
# A=5 and G= M
# A=2 and G=F

A = int(input("A: "))
G = input("M/F: ")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")
elif(A == 5 and G == "M"):
    print("fee is 300")
else:
    print("no fee")