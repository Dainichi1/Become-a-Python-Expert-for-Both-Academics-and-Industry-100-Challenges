# Esempio di calcolo hash
def hash_function(x):
    return x % 10

# Valori da inserire
values = [5, 10, 21, 15, 3, 11]

# Calcolo delle posizioni nella hash table
hash_table = {}
for value in values:
    index = hash_function(value)
    if index in hash_table:
        # Gestione collisione: usare una lista per memorizzare più elementi nello stesso indice
        hash_table[index].append(value)
    else:
        hash_table[index] = [value]

print(hash_table)
# Output esempio: {5: [5], 0: [10], 1: [21, 11], 0: [10, 15], 3: [3]}

# Utilizzo di un set e operazioni su di esso
s = {10, 20, 30, 40, 50}
print(s)  # Output: {50, 20, 40, 10, 30}

# Aggiungere elementi al set
s.add(60)
print(s)  # Output: {50, 20, 40, 10, 60, 30}

s.add(70)
print(s)  # Output: {50, 20, 70, 40, 10, 60, 30}

# Esempio di hash con modulo 16
def hash_function_mod16(x):
    return x % 16

# Calcolo hash per vari valori
hash_values = {10: hash_function_mod16(10),
               20: hash_function_mod16(20),
               30: hash_function_mod16(30),
               40: hash_function_mod16(40),
               50: hash_function_mod16(50),
               60: hash_function_mod16(60),
               70: hash_function_mod16(70)}

print(hash_values)
# Output esempio: {10: 10, 20: 4, 30: 14, 40: 8, 50: 2, 60: 12, 70: 6}
