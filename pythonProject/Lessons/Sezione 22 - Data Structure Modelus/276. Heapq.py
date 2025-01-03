import heapq  # Importa il modulo heapq

# Creazione di una lista
H = [10, 20, 50, 40, 60, 30, 70]

# heapify(): Converte la lista in un heap (priorità più bassa ha il numero più piccolo)
heapq.heapify(H)
print("Heap creato:", H)  # Output: [10, 20, 30, 40, 60, 50, 70]

# heappush(): Aggiunge un elemento all'heap mantenendo la struttura
heapq.heappush(H, 25)
print("Heap dopo heappush(25):", H)  # Output: [10, 20, 25, 40, 60, 50, 70, 30]

# heappop(): Rimuove e restituisce l'elemento con la priorità più alta (il numero più piccolo)
smallest = heapq.heappop(H)
print("Elemento rimosso con heappop():", smallest)  # Output: 10
print("Heap dopo heappop():", H)  # Output: [20, 30, 25, 40, 60, 50, 70]

# heapreplace(): Rimuove l'elemento con priorità più alta e lo sostituisce con un nuovo elemento
replaced = heapq.heapreplace(H, 35)
print("Elemento sostituito con heapreplace():", replaced)  # Output: 20
print("Heap dopo heapreplace(35):", H)  # Output: [25, 30, 35, 40, 60, 50, 70]

# nlargest(): Restituisce i 2 numeri più grandi nell'heap
largest = heapq.nlargest(2, H)
print("I 2 numeri più grandi:", largest)  # Output: [70, 60]

# nsmallest(): Restituisce i 3 numeri più piccoli nell'heap
smallest_three = heapq.nsmallest(3, H)
print("I 3 numeri più piccoli:", smallest_three)  # Output: [25, 30, 35]
