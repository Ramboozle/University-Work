# Last week you wrote a program that processed a collection of temperature readings
#  entered by the user and displayed the maximum, minimum, and mean. Create a
#  version of that program that takes the values from the command-line instead. Be
#  sure to handle the case where no arguments are provided!

import sys
from statistics import mean

sysargs = sys.argv[1:] # takes the arguments from the command line
temps = [num.strip('c') for num in sysargs] # removes the 'c' from the numbers
temps = [int(num) for num in temps] # converts the numbers to integers
print (temps)


if len(sysargs) == 0: # checks if the user did not enter any temperatures
    print('No temperatures provided')
    sys.exit(1) # exits the program if the user did not give any arguments


print('Max:', max(temps), 'C')
print('Min:', min(temps), 'C') # prints the max and min values
print('Mean:', mean(temps), 'C') # prints the mean value
