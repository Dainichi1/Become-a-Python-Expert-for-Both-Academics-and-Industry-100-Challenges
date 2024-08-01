item = input('Enter the item: ')
price = input('Enter the price: ')


tot = len(item) + len(price)




print(tot)

dots = '.' * (25-tot)

print(item+dots+price)