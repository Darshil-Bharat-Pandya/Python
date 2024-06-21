Marks = int(input("Please Enter Your Marks: "))

if(Marks <= 100 and Marks >=90):
    print("A1")
elif(Marks <= 89 and Marks >=80):
    print("A2")
elif(Marks <= 79 and Marks >=70):
    print("B1")
elif(Marks <= 69 and Marks >=60):
    print("B2")
elif(Marks <= 59 and Marks >=50):
    print("C1")
elif(Marks <= 49 and Marks >=40):
    print("C2")
elif(Marks <= 39 and Marks >=33):
    print("D")
else:
    print("Fail")    
