import bisect

# Lista ordinata
L = [10, 20, 20, 30, 50, 60, 70, 90]

# bisect.insort_left(): Inserisce un elemento nella lista mantenendo l'ordine
# Inserisce 90 alla posizione più a sinistra (prima di eventuali altri 90)
bisect.insort_left(L, 90)
print("Lista dopo insort_left(90):", L)  # Output: [10, 20, 20, 30, 50, 60, 70, 90, 90]

# bisect.insort_right(): Inserisce un elemento nella lista mantenendo l'ordine
# Inserisce 90 alla posizione più a destra (dopo tutti gli altri 90)
bisect.insort_right(L, 90)
print("Lista dopo insort_right(90):", L)  # Output: [10, 20, 20, 30, 50, 60, 70, 90, 90, 90]

# bisect_left(): Restituisce la posizione dove inserire un elemento mantenendo l'ordine
position_left = bisect.bisect_left(L, 90)
print("Posizione di inserimento per 90 (a sinistra):", position_left)  # Output: 7

# bisect_right(): Restituisce la posizione dove inserire un elemento mantenendo l'ordine
position_right = bisect.bisect_right(L, 90)
print("Posizione di inserimento per 90 (a destra):", position_right)  # Output: 10

# bisect(): Alias di bisect_right() per trovare la posizione di inserimento
position = bisect.bisect(L, 90)
print("Posizione di inserimento per 90 (bisect):", position)  # Output: 10

# Verifica degli ID degli elementi per mostrare che i duplicati sono posizioni diverse
print("ID di L[9]:", id(L[9]))  # Output: ID specifico del 90 in posizione 9
print("ID di L[10]:", id(L[10]))  # Output: ID specifico del 90 in posizione 10
