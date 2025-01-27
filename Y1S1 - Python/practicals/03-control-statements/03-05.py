BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
passwordValid = False
password1Valid = False
password2Valid = False

def check_password(password):
    if len(password) < 8 or len(password) > 12:
        print('Entered password is too short, Try Again with a password between 8 and 12 characters')
        return False
    if password in BAD_PASSWORDS:
        print('Password is too common, Try Again with a different password')
        return False
    return True

while not passwordValid:
    password1 = input('Please enter your new password:\n')
    password1Valid = check_password(password1)
    while not password1Valid:
        password1 = input('Please enter your new password:\n')
        password1Valid = check_password(password1)
    password2 = input('Please re-enter your password:\n')
    password2Valid = check_password(password2)
    while not password2Valid:
        password2 = input('Please re-enter your password:\n')
        password2Valid = check_password(password2)
    if password1 == password2:
        passwordValid = True
        print('Password set')
