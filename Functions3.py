# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Input principal amount
principal = float(input("Enter the principal amount: "))

# Input time period in years
time = float(input("Enter the time period in years: "))

# Check if the person is a senior citizen
is_senior_citizen = input("Are you a senior citizen? (yes/no): ").lower()

# Define interest rates
if is_senior_citizen == "yes":
    rate = 12  # 12% interest rate for senior citizens
else:
    rate = 10  # 10% interest rate for others

# Calculate and print simple interest
simple_interest = calculate_simple_interest(principal, rate, time)
print(f"Simple Interest: {simple_interest}")
