 # The Unix nl command prints the lines of a text file with a line number at the start
 # of each line. (It can be useful when printing out programs for dry runs or white-box
 # testing). Write an implementation of this command. It should take the name of the
 # files as a command-line argument.

import sys
file = sys.argv[1]
print(file)
lineNum = 0
with open(file) as f:
    for line in f:
        lineNum = lineNum + 1
        print(lineNum, line, end = '')