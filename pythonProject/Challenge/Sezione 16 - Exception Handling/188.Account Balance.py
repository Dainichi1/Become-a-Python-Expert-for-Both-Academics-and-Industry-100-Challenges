class AccountBalanceException(Exception):
    pass

def withdraw(amount):
    min = 5000
    balance = 10000
    op = balance - amount
    if op < min:
        raise AccountBalanceException('Amount in your bank account cannot be less than 5000')
    else:
        print('Remaining balance is: ',op)


amount = int (input('Enter the amount you want to withdrawn: '))

try:
    withdraw(amount)

except AccountBalanceException as e:
    print (e)