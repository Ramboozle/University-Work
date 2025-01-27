# Write a program that decrypts messages encoded as above.
# ('hbrqbebrqblbrqblbrqbobrqb wbrqbobrqbrbrqblbrqbdbrqb', 4) should return 'hello world'

def decrypt(inputStr, interval):
    key = inputStr[1:interval+1]
    return inputStr.replace(key, "")

print(decrypt('hbrqbebrqblbrqblbrqbobrqb wbrqbobrqbrbrqblbrqbdbrqb', 4))