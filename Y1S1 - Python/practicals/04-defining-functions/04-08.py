# Modify the previous program so that it can process any number of values. The input
# terminates when the user just pressed "Enter" at the prompt rather than entering a
# value.

from statistics import mean

temps = [] # create an empty list to store the temperatures
while True: # infinite loop
    temp = input('Enter a new temperature: ') # ask the user for a temperature
    if temp == '': # check if the user just pressed Enter
        break # breaks the loop if the user just pressed Enter
    else:
        while temp[-1] != 'C':  # check if the temperature ends in C
            print(temp,
                  'Invalid input - not ending in C')  # print an error message and asks the user to enter a temperature again
            temp = input('Enter a temperature again: ')
    temps.append(temp) # add the temperature to the list

print('Max:', max(temps))
print('Min:', min(temps)) # prints the max and min values
print('Mean:', mean([int(temp[:-1]) for temp in temps]), 'C')
# converts the string to an integer and removes the C, then calculates the mean