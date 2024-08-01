food = ['pizza','nuggets','hotdog','noodles','pasta','burger']

letter = input('Digit a letter: ')

for x in food:
    if x.startswith(letter):

        print(x)
