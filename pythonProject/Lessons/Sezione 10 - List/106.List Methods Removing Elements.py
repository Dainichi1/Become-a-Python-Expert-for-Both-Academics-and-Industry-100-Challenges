# Metodo pop()
# Rimuove l'ultimo elemento della lista se l'indice non è specificato
# Altrimenti, rimuove l'elemento all'indice specificato

L1 = [5, 6, 7, 8]
print(L1.pop())  # Output: 8
print(L1)  # Output: [5, 6, 7]

print(L1.pop(0))  # Output: 5
print(L1)  # Output: [6, 7]

print(L1.pop(1))  # Output: 7
print(L1)  # Output: [6]

# Keyword del
# Utilizzata per eliminare un elemento dalla lista
# La slicing funziona anche con la keyword del

L1 = [5, 6, 7, 8, 9]
del L1[3]
print(L1)  # Output: [5, 6, 7, 9]

del L1[0:2]
print(L1)  # Output: [7, 9]

# Metodo remove(x)
# Rimuove il primo elemento uguale a x dalla lista
# Genera un errore se l'elemento non è trovato

L1 = [5, 6, 7, 5, 6, 7]
L1.remove(6)
print(L1)  # Output: [5, 7, 5, 6, 7]

try:
    L1.remove(10)
except ValueError as e:
    print(e)  # Output: list.remove(x): x not in list

# Metodo clear()
# Cancella tutti gli elementi della lista

L1 = [5, 7, 5, 6, 7]
L1.clear()
print(L1)  # Output: []

L1 = [5, 6, 7, 8, 9, 10]
del L1[:]
print(L1)  # Output: []
