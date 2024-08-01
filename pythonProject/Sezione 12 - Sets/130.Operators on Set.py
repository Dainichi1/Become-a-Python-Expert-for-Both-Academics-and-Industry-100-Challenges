# Definizione di set
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
A = {1, 2, 3, 5, 7}
B = {5, 7, 9, 10, 11}

# Unione di A e B
C = A | B
print("Union:", C)  # Output: {1, 2, 3, 5, 7, 9, 10, 11}

# Intersezione di A e B
C = A & B
print("Intersection:", C)  # Output: {5, 7}

# Differenza tra A e B
C = A - B
print("Difference:", C)  # Output: {1, 2, 3}

# Differenza simmetrica tra A e B
C = A ^ B
print("Symmetric Difference:", C)  # Output: {1, 2, 3, 9, 10, 11}

# Operatori di confronto tra set
print("A < B:", A < B)   # False
print("B > A:", B > A)   # False
print("A <= s:", A <= s) # True
print("B <= s:", B <= s) # False
print("s == s:", s == s) # True
print("A == A:", A == A) # True
print("B != A:", B != A) # True
print("A >= B:", A >= B) # False

# Operatori di appartenenza
print("8 in S:", 8 in s)         # True
print("11 in S:", 11 in s)       # False
print("11 in B:", 11 in B)       # True
print("11 not in S:", 11 not in s) # True

# Nota sui risultati immagazzinati in A
A = A | B  # Unione
A = A & B  # Intersezione
A = A - B  # Differenza
