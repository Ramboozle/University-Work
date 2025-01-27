# Modify your "greetings" program so that the first letter of the name entered is
# always in uppercase with the rest in lowercase. This should happen even if the user
# entered their name differently. So if the user entered arthur, ARTHUR, or even
# arTHur the name should be displayed as Arthur.

Name = input("Enter your name: ")
print('Hello ',Name)
print('Hello ',Name.capitalize()) # converts the first character of a string to uppercase and the rest to lowercase