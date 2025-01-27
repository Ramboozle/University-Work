 # The Unix diff command compares two files and reports the differences, if any.
 # Write a simple implementation of this that takes two file names as command-line
 # arguments and reports whether or not the two files are the same. (Define "same" as
 # having the same contents.

import sys

def compare_files(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    max_len = max(len(lines1), len(lines2))
    differences = []

    for i in range(max_len):
        line1 = lines1[i] if i < len(lines1) else ''
        line2 = lines2[i] if i < len(lines2) else ''
        if line1 != line2:
            differences.append((i + 1, line1, line2))

    return differences

file1 = sys.argv[1]
file2 = sys.argv[2]
differences = compare_files(file1, file2)

if differences:
    print("The files are different. Differences:")
    for line_num, line1, line2 in differences:
        print(f"Line {line_num}:\nFile1: {line1} \nFile2: {line2}")
else:
    print("The files are the same.")