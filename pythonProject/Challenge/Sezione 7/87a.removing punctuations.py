

s1 = "'[torquati79@yahoo.it]'"

punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

newString = []

for letter in s1:
    if letter not in punctuations:
        newString.append(letter)


space=''
v = space.join(newString)

print(v)