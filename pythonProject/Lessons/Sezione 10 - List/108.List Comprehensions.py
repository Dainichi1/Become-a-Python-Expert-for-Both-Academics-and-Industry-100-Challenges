# List Comprehension
# È un metodo per creare liste in modo semplice da liste esistenti (o altri iterabili).
# Una lista può essere generata da una lista, tuple, stringa o set.
# Una lista può essere vuota, è denotata come [].
# Il metodo append() nella lista aggiunge un elemento alla lista.
# Un ciclo può essere utilizzato per aggiungere valori a una lista di un intervallo particolare.

# Esempio 1:
L1 = []
for x in range(10):
    L1.append(x)
print(L1)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Il processo sopra può essere fatto in modo semplice usando la "List Comprehension"

# Sintassi della List Comprehension:
# L1 = [espressione per elemento in iterabile]

# Esempio 2:
L1 = [x for x in range(10)]
print(L1)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Possiamo osservare da questo esempio come usando la list comprehension abbiamo semplificato l'esempio 1.
# Altri esempi di list comprehension sono:

# Esempio 3:
L2 = [x**2 for x in range(1, 6)]
print(L2)  # Output: [1, 4, 9, 16, 25]

# Esempio 4:
L3 = [x for x in (10, 5, 7, 8, 12, 13) if x % 2 == 0]
print(L3)  # Output: [10, 8, 12]

# Esempio 5:
L4 = [x.lower() for x in 'Python']
print(L4)  # Output: ['p', 'y', 't', 'h', 'o', 'n']

# Puoi anche leggere una lista da una tastiera
# Supponiamo di voler prendere input da tastiera (che è di tipo str) e convertirlo in lista.
# Questo può essere fatto in modo semplice usando la list comprehension.

# Esempio 6:
L5 = input("Enter names: ").split()
print(L5)  # Output: ['john', 'james', 'gregg'] (dipende dall'input fornito)
