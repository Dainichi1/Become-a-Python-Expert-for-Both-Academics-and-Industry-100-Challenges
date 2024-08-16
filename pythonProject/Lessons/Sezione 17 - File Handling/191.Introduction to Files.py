file = open('MyData.txt', 'r') # 'r' = read
str1 = file.read()
print(str1)

file2 = open('MyData.txt', 'r') # 'r' = read
str2 = file.read(6) # legge le prime 6 lettere
print(str2)

file.close()
file2.close()
