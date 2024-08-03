# Creazione di un dizionario vuoto
dict1 = dict()
print(dict1)  # Output: {}

# Un altro modo per creare un dizionario vuoto
dict5 = {}
print(dict5)  # Output: {}

# Creazione di un dizionario usando coppie di elementi iterabili
dict2 = dict(((1, 2), (2, 4), (3, 6)))
print(dict2)  # Output: {1: 2, 2: 4, 3: 6}

# Creazione di un dizionario usando zip per combinare due iterabili
l1 = ['A', 'B', 'C']
l2 = ['apple', 'ball', 'cat']
dict3 = dict(zip(l1, l2))
print(dict3)  # Output: {'A': 'apple', 'B': 'ball', 'C': 'cat'}
