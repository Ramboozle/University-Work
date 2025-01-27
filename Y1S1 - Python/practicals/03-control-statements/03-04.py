BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

def check_password(password):
    if len(password) < 8 or len(password) > 12:
        print('Entered password is too short')
        return False
    if password in BAD_PASSWORDS:
        print('Password is too common')
        return False
    return True

password1 = input('Please enter your new password:\n')

if not check_password(password1):
    exit()

password2 = input('Please re-enter your password:\n')

if not check_password(password2):
    exit()
if password1 == password2:
    print('Password set')
else:
    print('Passwords do not match')