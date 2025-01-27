# Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions. (Google will find you the formulae).

def celToFah(cel):
    """ Takes a temperature in C and returns it in F"""
    # (0°C × 9 / 5) + 32 = 32°F
    return (cel * 9/5) + 32

def fahToCel(Fah):
    """ Takes a temperature in F and returns it in C"""
    # (32°F − 32) × 5/9 = 0°C
    return (Fah - 32) * 5/9

print(celToFah(25)) # expected is 77
print(fahToCel(77)) # expected is 25