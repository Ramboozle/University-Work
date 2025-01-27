# code is horrid, but the output is neatly formatted :D

for i in range(14):
    mph = (i+1)*5
    kmh = round(((i + 1) * 5) * 1.60934)
    if mph < 9:
        print(f"|mph :{mph}  |kmh:{kmh}   |")
    elif kmh > 100:
        print(f"|mph: {mph} |kmh:{kmh} |")
    else:
        print(f"|mph :{mph} |kmh:{kmh}  |")