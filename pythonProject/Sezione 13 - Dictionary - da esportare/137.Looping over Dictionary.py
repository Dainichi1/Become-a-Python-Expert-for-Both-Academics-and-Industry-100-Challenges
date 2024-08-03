# Creazione di un dizionario
dict1 = {
    101: 'Production',
    102: 'Accounts',
    103: 'Sales & Marketing',
    104: 'Inventory'
}

# Iterazione attraverso le chiavi del dizionario
for x in dict1:
    print(x)  # Output: 101, 102, 103, 104 (uno per riga)

# Iterazione attraverso chiavi e valori del dizionario
for x in dict1:
    print(x, dict1[x])
    # Output:
    # 101 Production
    # 102 Accounts
    # 103 Sales & Marketing
    # 104 Inventory

# Utilizzo del metodo get() per accedere ai valori
for x in dict1:
    print(x, dict1.get(x))
    # Output: come sopra

# Differenza tra accesso con chiavi e metodo get()
print(dict1[102])  # Output: Accounts

try:
    print(dict1[106])  # Genera un KeyError
except KeyError as e:
    print(f"KeyError: {e}")  # Output: KeyError: 106

print(dict1.get(106))  # Output: None
print(dict1.get(106, 'Unknown Dept'))  # Output: Unknown Dept

# Uso di metodi keys(), values() e items() per iterare sul dizionario
print(dict1.keys())   # Output: dict_keys([101, 102, 103, 104])
print(dict1.values()) # Output: dict_values(['Production', 'Accounts', 'Sales & Marketing', 'Inventory'])
print(dict1.items())  # Output: dict_items([(101, 'Production'), (102, 'Accounts'), (103, 'Sales & Marketing'), (104, 'Inventory')])

# Iterazione attraverso chiavi e valori usando items()
for k, v in dict1.items():
    print(k, v)
    # Output: come sopra
