A = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]

B = []

for i in range(len (A[0])):
    s = []
    for j in range(len (A)):
        s.append(A[j][i])
    B.append(s)
print(B)
