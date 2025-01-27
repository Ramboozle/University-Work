password1 = input('Please enter your new password:\n')
password2 = input('Please re-enter your password:\n')
if password1 == password2:
    print('Password set')
else:
    print('Passwords do not match')