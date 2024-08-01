alpha = input('Enter the alphabet: ')

lower = []
upper = []

for letter in alpha:
    if letter.islower():
        lower.append(letter)
    else:
        upper.append(letter)

space =''

u = space.join(lower)
v = space.join(upper)

print(u+v)
