import copy

# Creazione di una lista
L = [10, 20, 30, 40, 50]

# Creazione di una copia superficiale usando copy.copy()
L1 = copy.copy(L)
print("L:", L)    # Output: [10, 20, 30, 40, 50]
print("L1:", L1)  # Output: [10, 20, 30, 40, 50]

# Controllo degli ID delle liste (L e L1 hanno ID diversi)
print("ID di L:", id(L))    # ID diverso
print("ID di L1:", id(L1))  # ID diverso

# Modifica di un elemento nella lista L
L[0] = 100
print("L dopo modifica:", L)    # Output: [100, 20, 30, 40, 50]
print("L1 dopo modifica di L:", L1)  # Output: [10, 20, 30, 40, 50] (rimane invariata)

# Controllo degli ID degli oggetti nelle liste
print("ID di L[1]:", id(L[1]))    # Output: ID uguale a quello di L1[1]
print("ID di L1[1]:", id(L1[1]))  # Output: ID uguale a quello di L[1]
