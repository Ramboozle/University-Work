# Write a function that has a single string as its parameter, and returns the number of
# uppercase letters, and the number of lowercase letters in the string. Test the
# function with a short program.

def count_case(string):
    """ Function to count the number of uppercase and lowercase letters in a string """
    upper = 0 # Defines the counters for uppercase and lowercase letters
    lower = 0
    for char in string: # iterate through each character in the string
        if char.isupper(): # check if the character is uppercase
            upper += 1 # increment the uppercase counter
        elif char.islower(): # check if the character is lowercase
            lower += 1 # increment the lowercase counter

    return upper, lower  # return the values of both counters

print(count_case("Hello, World!"))