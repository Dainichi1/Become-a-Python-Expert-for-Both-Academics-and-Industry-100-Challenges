import random

npc = random.randint(1,10)
nhu = 0

while nhu != npc:
    nhu = int (input('Enter a number between 1 and 10: '))
    if nhu > npc :
        print ('Your number is greater than mine')
    elif nhu < npc :
        print ('Your number is less than mine')
    else :
        print ('You guessed the number! My number: ',npc,', your number: ',nhu)