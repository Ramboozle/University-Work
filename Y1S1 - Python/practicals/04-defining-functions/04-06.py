# Write a program that takes a centigrade temperature and displays the equivalent in
# fahrenheit. The input should be a number followed by a letter C. The output should
# be in the same format.
from logging.config import valid_ident

def celtofah(input):
    if input[-1] != 'C':
        return 'Invalid Input'
    else:
        return str((int(input[:-1]) * 9/5) + 32) + 'F'

print(celtofah(input('Please enter a temperature ending in C : ')))