# Input string
input_string = "Hello, world. How are you?"

# Replace comma with a placeholder (e.g., '#')
temp_string = input_string.replace(",", "#")

# Replace period with comma
temp_string = temp_string.replace(".", ",")

# Replace placeholder with period
output_string = temp_string.replace("#", ".")

# Display the modified string
print(output_string)
