# Creazione di un dizionario con coppie chiave-valore
dict1 = {'fruit': 'apple', 'vegetable': 'carrot', 'dish': 'salad'}

# Accesso ai valori utilizzando le chiavi
print(dict1['fruit'])      # Output: apple
print(dict1['vegetable'])  # Output: carrot
print(dict1['dish'])       # Output: salad

# Creazione di un secondo dizionario
dict2 = {101: 'John', 102: 'Smith', 103: 'Mark', 104: 'David'}

# Accesso a un valore usando una chiave
print(dict2[102])  # Output: Smith

# Gestione di chiavi inesistenti (genera un errore)
try:
    print(dict2[0])
except KeyError as e:
    print(f"KeyError: {e}")  # Output: KeyError: 0

# Aggiornamento di un valore nel dizionario
dict2[103] = 'Mathew'
print(dict2)  # Output: {101: 'John', 102: 'Smith', 103: 'Mathew', 104: 'David'}

# Inserimento di una nuova coppia chiave-valore
dict2[105] = 'Ajay'
print(dict2)  # Output: {101: 'John', 102: 'Smith', 103: 'Mathew', 104: 'David', 105: 'Ajay'}

# Eliminazione di un elemento dal dizionario usando la chiave
del dict2[104]
print(dict2)  # Output: {101: 'John', 102: 'Smith', 103: 'Mathew', 105: 'Ajay'}


# Iterazione attraverso le chiavi del dizionario
for i in dict2:
    print(i)  # Output: 101, 102, 103, 105 (uno per riga)

# Iterazione attraverso le chiavi e i valori del dizionario
for i in dict2:
    print(i, dict2[i])  # Output: 101 John, 102 Smith, 103 Mathew, 105 Ajay (uno per riga)
