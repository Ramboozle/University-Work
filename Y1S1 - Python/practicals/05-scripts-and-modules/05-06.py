# Write a program that takes the name of a file as a command-line argument, and
#  creates a backup copy of that file. The backup should contain an exact copy of the
#  contents of the original and should, obviously, have a different name.
#  Hint: By now, you should be getting the idea that there is a built-in way to do the
#  heavy lifing here! Take a look at the "Brief Tour of the Standard Library" in the docs.

import sys, os, shutil

if len(sys.argv) != 2: 
    print("The correct usage is: 05-06.py <filename>")
    sys.exit(1)

print ("Creating backup of file: ", sys.argv[1])
scriptPath = os.path.dirname(os.path.abspath(__file__))
shutil.copy2(sys.argv[1], scriptPath + "/" + sys.argv[1] + ".bak")
print ("Backup created with the name: ", sys.argv[1] + ".bak")
