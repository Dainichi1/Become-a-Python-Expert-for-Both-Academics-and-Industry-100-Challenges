emailid = input('Enter your e-mail id: ')

atposition = emailid.find('@')



print(atposition)

print('userid: ',emailid[:atposition:])
print('domain: ',emailid[atposition+1::])





