original_string = "Hello, World!"
stack = list(original_string)
reversed_string = ""
while stack:
    reversed_string += stack.pop()
print(reversed_string)
