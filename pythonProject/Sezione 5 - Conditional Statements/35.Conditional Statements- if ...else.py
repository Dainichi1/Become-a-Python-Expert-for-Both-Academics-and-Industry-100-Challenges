while True:
    a = int (input('Enter a number: '))
    if a < 0 :
        print ('The number ',a,' is negative')
    elif  a == 0:
        print('You entered zero')
    else :
        print ('The number ',a,' is positive')



    keep = input('Press c to continue or any other letter to quit: ')
    if keep.lower() != 'c':
        break