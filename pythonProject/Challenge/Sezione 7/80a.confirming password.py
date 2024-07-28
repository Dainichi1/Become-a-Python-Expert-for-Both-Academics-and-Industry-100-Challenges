pass1 = input('Enter password: ')
pass2 = input('Enter the password one more time:')

if pass1 == pass2:
    print('ok')
else:
    print('error')

if pass1.casefold() == pass2.casefold():
    print('check for the cases case')
else:
    print('passwords are different')