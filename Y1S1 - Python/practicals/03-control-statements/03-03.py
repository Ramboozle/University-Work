password1 = input('Please enter your new password:\n')
if len(password1) < 8 or len(password1) > 12:
    print('Entered password is too short')
    exit()
password2 = input('Please re-enter your password:\n')
if len(password2) < 8 or len(password2) > 12:
    print('Entered password is too short')
    exit()
if password1 == password2:
    print('Password set')
else:
    print('Passwords do not match')