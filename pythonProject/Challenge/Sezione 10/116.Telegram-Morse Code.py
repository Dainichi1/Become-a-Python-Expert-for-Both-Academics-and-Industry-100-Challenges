morse_array = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---']

text = 'deface'

morse_str=''

for x in text:
    morse_str+=morse_array[ord(x)-97] + " "
print(morse_str)