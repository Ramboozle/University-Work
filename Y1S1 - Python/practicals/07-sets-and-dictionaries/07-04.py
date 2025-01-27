# One approach to analysing some encrypted data where a substitution is suspected
#  is frequency analysis. A count of the different symbols in the message can be used
#  to identify the language used, and sometimes some of the letters. In English, the
#  most common letter is "e", and so the symbol representing "e" should appear most
#  in the encrypted text.
#  Write a program that processes a string representing a message and reports the six
#  most common letters, along with the number of times they appear. Case should
#  not matter, so "E" and "e" are considered the same.
#  Hint: There are many ways to do this. It is obviously a dictionary, but we will want
#  zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
#  best to ignore that initially, and then check the usual resources for the runes.

def frequency_analysis(message):
    message = message.lower() # converts the message to lowercase
    frequency = {}
    for letter in message: # iterates through each character in the message
        if letter.isalpha(): # checks if the character is a letter
            if letter in frequency: # checks if the letter is already in the dictionary
                frequency[letter] += 1 # increments the count of the letter if so
            else:
                frequency[letter] = 1
    return dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:6])

print(frequency_analysis('The quick brown fox jumps over the lazy dog.'))