# Esempio di liste eterogenee
Mylist = ['john', 'smith', 'mark', 'eric', 'smith']
print(Mylist)

# Conversione di un tuple in una lista
list1 = list((1, 2, 3, 4, 5))
print(list1)

# Accesso agli elementi della lista
print(Mylist[2])   # Output: 'mark'
print(Mylist[-2])  # Output: 'eric'

# Le liste sono eterogenee
Mylist = ['John', 15, 14.6, True, 'Steven', 5 + 7j]
print(Mylist)

# Le liste sono mutabili
Mylist = [15, 9, 12, 18, 7, 10]
print(Mylist)

# Modifica del primo elemento
Mylist[0] = 30
print(Mylist)

# Modifica del quinto elemento
Mylist[4] = 'john'
print(Mylist)

# Lunghezza della lista
print(len(Mylist))

# Appendere un elemento alla lista
Mylist = [1, 2, 3, 4, 5, 6]
Mylist.append(50)
print(Mylist)
