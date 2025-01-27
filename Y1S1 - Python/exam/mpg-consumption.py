import sys
file = sys.argv[1]
#file = "fuel.txt"
total = (0.0)
with open(file) as f:
    for line in f:
        total = total + float(line)
    print(f"The Average is {total/len(file)}")