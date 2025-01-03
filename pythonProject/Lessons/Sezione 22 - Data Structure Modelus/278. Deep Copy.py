import copy

# Creazione di una lista annidata
L = [[10, 20], [30, 40], [50, 60]]

# Creazione di una deep copy usando copy.deepcopy()
L1 = copy.deepcopy(L)
print("L:", L)    # Output: [[10, 20], [30, 40], [50, 60]]
print("L1:", L1)  # Output: [[10, 20], [30, 40], [50, 60]]

# Controllo degli ID delle liste
print("ID di L:", id(L))    # ID diverso
print("ID di L1:", id(L1))  # ID diverso

# Modifica di un elemento nella lista originale
L[0][0] = 100
print("L dopo modifica:", L)    # Output: [[100, 20], [30, 40], [50, 60]]
print("L1 dopo modifica di L:", L1)  # Output: [[10, 20], [30, 40], [50, 60]] (rimane invariata)
