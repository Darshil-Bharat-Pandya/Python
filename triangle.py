s1 = float(input("Please enter the value: "))
s2 = float(input("Please enter the value: "))
s3 = float(input("Please enter the value: "))

# s = sides of the triangle

s = (s1 + s2 + s3) / 2 

# area = area of the triangle

area = (s*(s-s1)*(s-s2)*(s-s3)) ** 0.5

print("The area of the tiangle is",round(area,2))
