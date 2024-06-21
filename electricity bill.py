# Input the consumption units from the user
consumption_units = float(input("Enter the consumption units: "))

# Initialize variables for the bill and rate of charge
bill = 0
rate_of_charge = 0

# Determine the rate of charge based on consumption units
if consumption_units <= 150:
    rate_of_charge = 3
elif 151 <= consumption_units <= 300:
    rate_of_charge = 100 + (consumption_units - 150) * 3.75
elif 301 <= consumption_units <= 450:
    rate_of_charge = 250 + (consumption_units - 300) * 4
elif 451 <= consumption_units <= 600:
    rate_of_charge = 300 + (consumption_units - 450) * 4.25
else:
    rate_of_charge = 400 + (consumption_units - 600) * 5

# Calculate the bill amount
bill = consumption_units * rate_of_charge

# Print the bill amount
print(f"Your electricity bill for {consumption_units} units is Rs. {bill:.2f}")
