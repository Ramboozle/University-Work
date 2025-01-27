 # The Unix wc command counts the number of lines, words,and characters in a file.
 # Write an implementation of this that takes a file name as a command-line
 # argument, and then prints the number of lines and characters.
 # Note: Linux (and Mac) users can use the "wc" command to check the results of their
 # implementation

import sys

file = sys.argv[1]
lineNum = 0
charNum = 0
with open(file) as f:
    for line in f:
        lineNum = lineNum + 1
        charNum = charNum + len(line)
print(f"Lines: {lineNum}")
print(f"Characters: {charNum}")
