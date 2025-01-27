# Functions are often used to validate input. Write a function that accepts a single
# integer as a parameter and returns True if the integer is in the range 0 to 100
# (inclusive), or False otherwise. Write a short program to test the function.

def lessThan100(x):
    """ Returns True if x is within the range of 0 to 100, otherwise False """
    return 0 <= x <= 100

print(lessThan100(-1))
print(lessThan100(0))
print(lessThan100(100))
print(lessThan100(101))