# Input the person's age
age = int(input("Enter your age: "))

# Define the minimum voting age
voting_age = 18

# Check if the person is eligible to vote
if age >= voting_age:
    print("You are eligible to vote.")
else:
    years_left = voting_age - age
    print("You are not eligible to vote yet.")
    print(f"You will be eligible to vote in {years_left} years.")
