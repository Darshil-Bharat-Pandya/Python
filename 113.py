marks = int(input("\nPlease Enter Your Marks: "))

if (marks <= 100 and marks >= 90):
    print("\nGrade = A1")
elif (marks <= 89 and marks >= 80):
    print("\nGrade = A2")
elif (marks <= 79 and marks >= 70):
    print("\nGrade = B1")
elif (marks <= 69 and marks >= 60):
    print("\nGrade = B2")
elif (marks <= 59 and marks >= 50):
    print("\nGrade = C1")
elif (marks <= 49 and marks >= 40):
    print("\nGrade = C2")
elif (marks <= 39 and marks >= 33):
    print("\nGrade = D")
else:
    print("\nGrade = Fail")