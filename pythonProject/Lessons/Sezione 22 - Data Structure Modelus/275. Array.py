import array

# Creazione di un array di interi
ar1 = array.array('i', [10, 20, 30, 40])  # 'i' indica che l'array contiene interi
print("ar1:", ar1)  # Output: array('i', [10, 20, 30, 40])

# Creazione di un array di byte da una stringa
s1 = b'abcdef'  # Stringa in formato byte
ar2 = array.array('b', s1)  # 'b' indica che l'array contiene byte
print("ar2:", ar2)  # Output: array('b', [97, 98, 99, 100, 101, 102])

# Accesso a un elemento specifico dell'array
print("ar2[0]:", ar2[0])  # Output: 97 (ASCII di 'a')

# Accesso a un intervallo di elementi (slicing)
print("ar2[1:3]:", ar2[1:3])  # Output: array('b', [98, 99]) (ASCII di 'b' e 'c')

# Aggiunta di un elemento all'array
ar2.append(103)  # Aggiunge 103 (ASCII di 'g') all'array
print("ar2 dopo append:", ar2)  # Output: array('b', [97, 98, 99, 100, 101, 102, 103])

# Ricerca dell'indice di un valore specifico
index_102 = ar2.index(102)  # Trova l'indice del valore 102 (ASCII di 'f')
print("Indice di 102:", index_102)  # Output: 5

# Visualizzazione del typecode dell'array
print("Typecode di ar2:", ar2.typecode)  # Output: 'b' (tipo byte)
