# Write a program that reads 6 temperatures (in the same format as before), and
# displays the maximum, minimum, and mean of the values.
# Hint: You should know there are built-in functions for max and min. If you hunt, you
# might also find one for the mean.

from statistics import mean

temps = ['10C', '20C', '30C', '40C', '50C', '60C']

for temp in temps: # iterate through each temperature
    if temp[-1] != 'C': # check if the temperature ends in C
        print(temp, 'Invalid input - not ending in C')
        break # breaks the loop if the input is invalid
else:
    print('Max:', max(temps), 'C')
    print('Min:', min(temps), 'C') # prints the max and min values
    print('Mean:', mean([int(temp[:-1]) for temp in temps]), 'C') # converts the string to an integer and removes the C, then calculates the mean