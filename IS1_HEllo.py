str="Hello World"
for x in str:
    print(x)
    print("Position of each character in string:",str.index(x))
xoroperator=127^str.index(x)
print("Print the result of XOR operator:", xoroperator)

andoperator=127&str.index(x)
print("Print the result of AND operator:", andoperator)

oroperator=127|str.index(x)
print("Print the result of OR operator:", oroperator)