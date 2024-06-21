# Input strings
S1 = "Hello"
S2 = "World"

# Calculate the middle index of S1
middle_index = len(S1) // 2

# Create the new string S3 by appending S2 in the middle of S1
S3 = S1[:middle_index] + S2 + S1[middle_index:]

# Print the new string S3
print(S3)
