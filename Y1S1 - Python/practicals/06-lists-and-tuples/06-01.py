# Write a function that accepts a positive integer as a parameter and then returns a
#  representation of that number in binary (base 2)#

def binary(inputNum):
    if inputNum < 0:
        return "Invalid input: negative number"
    inputNum = bin(inputNum)
    return inputNum[2:]

print(binary(-10))
print(binary(10))
print(binary(5))
print(binary(3))