# Write a program that takes a bunch of command-line arguments, and then prints
# out the shortest. If there is more than one of the shortest length, any will do.
# Hint: Don't overthink this. A good way to find the shortest is just to sort them.

import sys
sys.argv.sort(key=len)
print(f"The shortest argument was{sys.argv[1]}") # The first argument is the script name, so we want the second argument