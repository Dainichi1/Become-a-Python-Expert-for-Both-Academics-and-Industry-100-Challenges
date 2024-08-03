# Iterare una lista significa visitare o accedere a tutti gli elementi della lista uno per uno.
# Questo processo è chiamato anche traversing.

# Creazione di una lista
list1 = [5, 6, 7, 8, 9]

# Iterazione tramite un ciclo for
for x in list1:
    print(x)
# Output:
# 5
# 6
# 7
# 8
# 9

# Iterazione usando il range
for i in range(len(list1)):
    print(list1[i])
# Output:
# 5
# 6
# 7
# 8
# 9

# Inizio dell'iterazione da un indice specifico
for i in range(2, len(list1)):
    print(list1[i])
# Output:
# 7
# 8
# 9

# Iterazione in ordine inverso
for i in range(len(list1)-1, -1, -1):
    print(list1[i])
# Output:
# 9
# 8
# 7
# 6
# 5
