file = open('ModeTypes.txt','r')

print(file.name)
print(file.mode)
print(file.closed)

line = file.readline() # legge una sola riga di testo
print(line)
line = file.readline()
print(line)

line = file.readlines()
print(line) #lista di stringhe



