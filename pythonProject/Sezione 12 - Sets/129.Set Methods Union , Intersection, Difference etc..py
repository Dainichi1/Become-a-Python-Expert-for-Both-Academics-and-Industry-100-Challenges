# Definizione di due set
s1 = {1, 2, 3, 5, 7}
s2 = {5, 7, 9, 10, 11}

# Unione di s1 e s2
union_set = s1.union(s2)
print("Union:", union_set)  # Output: {1, 2, 3, 5, 7, 9, 10, 11}

# Intersezione di s1 e s2
intersection_set = s1.intersection(s2)
print("Intersection:", intersection_set)  # Output: {5, 7}

# Differenza tra s1 e s2
difference_set = s1.difference(s2)
print("Difference:", difference_set)  # Output: {1, 2, 3}

# Differenza simmetrica tra s1 e s2
symmetric_difference_set = s1.symmetric_difference(s2)
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 3, 9, 10, 11}

# Aggiornamento dell'intersezione (modifica s1)
s1.intersection_update(s2)
print("Intersection Update (s1):", s1)  # Output: {5, 7}
