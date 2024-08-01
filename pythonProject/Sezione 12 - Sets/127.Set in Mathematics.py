# Definizione di un set
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Un set in matematica non può avere valori duplicati
A = {1, 2, 3, 5, 7}

# Verifica se A è un sottoinsieme di s
print(A.issubset(s))  # Output: True

# Definizione di un altro sottoinsieme
B = {5, 7, 9, 10}

# Verifica se B è un sottoinsieme di s
print(B.issubset(s))  # Output: True

# Definizione di un set uguale a s
c = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Verifica se c è uguale a s o è un sottoinsieme di s
print(c == s)          # Output: True
print(c.issubset(s))   # Output: True

# Definizione di un sottoinsieme proprio
D = {1, 2, 3, 4, 5}
E = {6, 7, 8, 9, 10}

# Verifica che D ed E siano sottoinsiemi propri di s
print(D.issubset(s) and D != s)  # Output: True
print(E.issubset(s) and E != s)  # Output: True

# Verifica se D ed E sono disgiunti (non hanno elementi in comune)
print(D.isdisjoint(E))  # Output: True
