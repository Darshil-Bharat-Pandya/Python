# Accessing elements of String in Python

# In python programming, the individual characters of a String can be accessed by using the method of Indexing. Negative Indexing allows negative address references to access characters from the back of the String, e.g. -1 refers to the last character, -2 refers to the second last character, and so on.

# Example: This Python code demonstartes how to work with a string named 'String1'. It initializes the string with "GeeksForGeeks" and prints it. It then showcases how to access the first character("G") using an index of 0 and the last character ("s") using a negative index of -1.

String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)
print("\nFirst character of String is: ")
print(String1[0])
print("\nLast character of String is: ")
print(String1[-1])