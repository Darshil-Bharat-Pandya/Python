# One Liner if elif else Statements.

# The one-liner if elif else statement in Python are used when there are a simple and straightforward conditions to be implemented. This means that the code can be fitted in a single line expression. It uses a Python dictionary like structure along with Python dictionary get() method.

# Syntax: This can be easily interpreted as if condition 1 is True run code 1 if condition 2 is True  code 2 and if both of them are false run the third code.

x = 0

result = {x > 0: "Positive", x < 0: "Negative"}.get(True, "Zero")

print(result)