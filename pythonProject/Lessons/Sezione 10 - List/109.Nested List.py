# Esempio di lista eterogenea e annidata
nested_list = [10, 20, ['a', 'b', ['c', 'd'], 30], 40]
print(nested_list)

# Rappresentazione diagrammatica di una lista annidata
# nested_list = [10, 20, ['a', 'b', ['c', 'd'], 30], 40]
# Indici:         0   1      2          3      4

# Accesso agli elementi della lista annidata
print(nested_list[2][2][1])  # Output: 'd'

# Operazioni su matrici (liste di liste)
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Somma di due matrici
C = []
for i in range(len(A)):
    S = []
    for j in range(len(A[0])):
        S.append(A[i][j] + B[i][j])
    C.append(S)

print(C)
# Output: [[10, 10, 10], [10, 10, 10], [10, 10, 10]]

# Operazioni come -, *, etc. su una matrice
# Sottrazione di due matrici
D = []
for i in range(len(A)):
    S = []
    for j in range(len(A[0])):
        S.append(A[i][j] - B[i][j])
    D.append(S)

print(D)
# Output: [[-8, -6, -4], [-2, 0, 2], [4, 6, 8]]

# Moltiplicazione di due matrici (element-wise)
E = []
for i in range(len(A)):
    S = []
    for j in range(len(A[0])):
        S.append(A[i][j] * B[i][j])
    E.append(S)

print(E)
# Output: [[9, 16, 21], [24, 25, 24], [21, 16, 9]]

# Divisione di due matrici (element-wise)
F = []
for i in range(len(A)):
    S = []
    for j in range(len(A[0])):
        S.append(A[i][j] / B[i][j])
    F.append(S)

print(F)
# Output: [[0.1111111111111111, 0.25, 0.42857142857142855], [0.6666666666666666, 1.0, 1.5], [2.3333333333333335, 4.0, 9.0]]
