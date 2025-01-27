# When processing data it is often useful to remove the last character from some
# input (it is often a newline). Write and test a function that takes a string parameter
# and returns it with the last character removed. (If the string contains one or fewer
# characters, return it unchanged.)

def removeLastChar(string):
    """ Function to remove the last character from a string """
    if len(string) <= 1: # checks the length of the string to see if it is one or less
        return string # returns the string unchanged
    else:
        return string[:-1] # returns the string with the last character removed

print(removeLastChar("Hello, World!"))
print(removeLastChar("R"))