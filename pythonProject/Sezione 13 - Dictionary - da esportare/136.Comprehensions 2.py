# Creazione di un dizionario usando enumerate, che associa indici agli elementi
l1 = ['apple', 'ball', 'cat']
dict4 = dict(enumerate(l1))
print(dict4)  # Output: {0: 'apple', 1: 'ball', 2: 'cat'}

# Dictionary comprehension di base
dict6 = {x: x**2 for x in range(5)}
print(dict6)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Usando tuple nella dictionary comprehension
dict7 = {(x, x+1): x**2 for x in range(3)}
print(dict7)  # Output: {(0, 1): 0, (1, 2): 1, (2, 3): 4}

# Usando zip per combinare due iterabili in una dictionary comprehension
l2 = ['A', 'B', 'C']
l3 = ['apple', 'ball', 'cat']
dict8 = {x: y for x, y in zip(l2, l3)}
print(dict8)  # Output: {'A': 'apple', 'B': 'ball', 'C': 'cat'}

# Usando enumerate all'interno di una dictionary comprehension
dict9 = {i: item for i, item in enumerate(l3)}
print(dict9)  # Output: {0: 'apple', 1: 'ball', 2: 'cat'}
