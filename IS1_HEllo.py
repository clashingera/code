# Define a string variable
str = "Hello World"

# Iterate through each character in the string
for x in str:
    # Print the current character
    print(x)
    # Print the position of the current character in the string
    print("Position of each character in string:", str.index(x))

# Calculate XOR operator between 127 and the index of the last character in the string
xoroperator = 127 ^ str.index(x)
# Print the result of XOR operator
print("Print the result of XOR operator:", xoroperator)

# Calculate AND operator between 127 and the index of the last character in the string
andoperator = 127 & str.index(x)
# Print the result of AND operator
print("Print the result of AND operator:", andoperator)

# Calculate OR operator between 127 and the index of the last character in the string
oroperator = 127 | str.index(x)
# Print the result of OR operator
print("Print the result of OR operator:", oroperator)
