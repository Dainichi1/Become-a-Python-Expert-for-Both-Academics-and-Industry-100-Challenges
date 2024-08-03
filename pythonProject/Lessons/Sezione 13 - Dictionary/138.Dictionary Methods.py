# Creazione di un dizionario di esempio
dict1 = {
    101: 'Production',
    102: 'Accounts',
    103: 'Sales & Marketing',
    104: 'Inventory'
}

# Metodo copy() - Creazione di una copia superficiale di un dizionario
dict2 = dict1.copy()
print(dict2)  # Output: {101: 'Production', 102: 'Accounts', 103: 'Sales & Marketing', 104: 'Inventory'}

# Modifica del dizionario copiato
dict2[102] = 'Designing'
print(dict1)  # Output: {101: 'Production', 102: 'Accounts', 103: 'Sales & Marketing', 104: 'Inventory'}
print(dict2)  # Output: {101: 'Production', 102: 'Designing', 103: 'Sales & Marketing', 104: 'Inventory'}

# Metodo update() - Aggiunta di più coppie chiave-valore
dict2 = {105: 'Designing', 106: 'Packaging'}
dict1.update(dict2)
print(dict1)
# Output: {101: 'Production', 102: 'Accounts', 103: 'Sales & Marketing', 104: 'Inventory', 105: 'Designing', 106: 'Packaging'}

# Metodo setdefault() - Ottenere il valore di una chiave o inserire una coppia chiave-valore se la chiave non esiste
dict1.setdefault(107, 'Adv')
print(dict1)
# Output: {101: 'Production', 102: 'Accounts', 103: 'Sales & Marketing', 104: 'Inventory', 105: 'Designing', 106: 'Packaging', 107: 'Adv'}

# Metodo formkeys() - Creazione di un nuovo dizionario da una sequenza di chiavi con un valore predefinito
L1 = [11, 22, 33, 44]
dict3 = dict.fromkeys(L1, 'hello')
print(dict3)
# Output: {11: 'hello', 22: 'hello', 33: 'hello', 44: 'hello'}

# Metodo pop() - Rimozione di una coppia chiave-valore usando la chiave specificata
dict1.pop(104)
print(dict1)
# Output: {101: 'Production', 102: 'Accounts', 103: 'Sales & Marketing', 105: 'Designing', 106: 'Packaging', 107: 'Adv'}

# Metodo popitem() - Rimozione dell'ultima coppia chiave-valore aggiunta
last_item = dict1.popitem()
print(last_item)  # Output: (107, 'Adv')
print(dict1)
# Output: {101: 'Production', 102: 'Accounts', 103: 'Sales & Marketing', 105: 'Designing', 106: 'Packaging'}

# Metodo clear() - Cancellazione di tutte le coppie chiave-valore dal dizionario
dict1.clear()
print(dict1)  # Output: {}

# Uso del comando del per eliminare completamente il dizionario
del dict1
try:
    print(dict1)  # Genera un errore perché dict1 è stato eliminato
except NameError:
    print("dict1 non è definito")
