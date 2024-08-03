# Creazione di un set vuoto
S = set()
print(S)  # Output: set()

# Set comprehension per creare un set con valori da 0 a 9
S1 = {x for x in range(10)}
print(S1)  # Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Set comprehension per ottenere il quadrato degli elementi
S2 = {x**2 for x in [-2, -1, 0, 1, 2]}
print(S2)  # Output: {0, 1, 4}

# Set comprehension con condizione per ottenere solo i numeri pari
S3 = {x for x in (10, 5, 7, 8, 12, 3) if x % 2 == 0}
print(S3)  # Output: {8, 10, 12}

# Set comprehension per ottenere le lettere maiuscole di una stringa
S4 = {x.upper() for x in 'philippines'}
print(S4)  # Output: {'P', 'H', 'I', 'L', 'N', 'E', 'S'}
