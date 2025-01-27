 # Write a program that, when run from the command line, reports how many
 # arguments were provided. (Remember that the program name itself isnotan
 # argument)

import sys
print(f"Number of arguments provided: {len(sys.argv)-1}")