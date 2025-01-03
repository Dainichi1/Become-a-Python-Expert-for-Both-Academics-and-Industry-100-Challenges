import copy

# Creazione di una classe Person
class Person:
    def __init__(self, name):
        self.name = name

# Creazione di una lista di oggetti Person
L = [Person("John"), Person("Tim"), Person("Jim")]

# Shallow Copy
L1 = copy.copy(L)
print("Shallow Copy:")
print("ID di L:", id(L))    # ID diverso
print("ID di L1:", id(L1))  # ID diverso
print("ID di L[0]:", id(L[0]))    # ID uguale a L1[0]
print("ID di L1[0]:", id(L1[0]))  # ID uguale a L[0]

# Modifica di un attributo in L
L[0].name = "Mike"
print("L[0].name:", L[0].name)    # Output: "Mike"
print("L1[0].name:", L1[0].name)  # Output: "Mike" (modifica riflessa nella shallow copy)

# Deep Copy
L2 = copy.deepcopy(L)
print("Deep Copy:")
print("ID di L:", id(L))    # ID diverso
print("ID di L2:", id(L2))  # ID diverso
print("ID di L[0]:", id(L[0]))    # ID diverso da L2[0]
print("ID di L2[0]:", id(L2[0]))  # ID diverso da L[0]

# Modifica di un attributo in L
L[0].name = "David"
print("L[0].name:", L[0].name)    # Output: "David"
print("L2[0].name:", L2[0].name)  # Output: "Mike" (deep copy non è influenzata)
