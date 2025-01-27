 # Another way to hide a message is to include the letters that make it up within
 # seemingly random text. The letters of the message might be every fifth character,
 # for example. Write and test a function that does such encryption. It should
 # randomly generate an interval (between 2 and 20), space the message out
 # accordingly, and should fill the gaps with random letters. The function should
 # return the encrypted message and the interval used.
 # For example, if the message is "send cheese", the random interval is 2, and for
 # clarity the random letters are not random:
 # send cheese
 # s  e  n  d   c  h  e  e  s  e
 # sxyexynxydxy cxyhxyexyexysxye

import random

def encrypt(inputStr):
    interval = random.randint(2, 20)
    alph = "abcdefghijklmnopqrstuvwxyz"
    randomstring=""
    for i in range(interval):
        randomstring = randomstring + random.choice(alph)
    encryptedMessage = ""
    for i in range(len(inputStr)):
        if inputStr[i] == " ":
            encryptedMessage = encryptedMessage + " "
        else:
            encryptedMessage = encryptedMessage + inputStr[i] +randomstring
    return encryptedMessage, interval

print(encrypt("Alina is the best"))