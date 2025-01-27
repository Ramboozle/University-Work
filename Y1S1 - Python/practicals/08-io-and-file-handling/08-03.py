# The Unix grep command searches a file and outputs the lines in the file that
#  contain a certain pattern. Write an implementation of this. It will take two
#  command-line arguments: the first is the string to look for, and the second is the
#  file name. The output should be the lines in the file that contain the string.

import sys

search_string = sys.argv[1]
fileToOpen = sys.argv[2]

with open(fileToOpen) as f:
    for line in f:
        if search_string in line:
            print(line, end = '')