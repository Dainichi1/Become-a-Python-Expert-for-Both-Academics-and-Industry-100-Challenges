# Funzione con tre argomenti obbligatori
def add(a, b, c):
    return a + b + c

# Esempi di chiamata della funzione 'add'
print(add(10, 5, 2))  # Funziona correttamente
# print(add(10, 5))    # Errore: manca un argomento (c)
# print(add(10))       # Errore: mancano due argomenti (b e c)

# Funzione con argomenti di default
def add_default(a, b=0, c=0):
    return a + b + c

# Esempi di chiamata della funzione 'add_default'
print(add_default(5, 7))           # Output: 12, prende a=5, b=7, c=0
print(add_default(a=10, b=5, c=2)) # Output: 17, assegna correttamente tutti i valori
# print(add_default(b=5, c=2, 10))  # Errore: gli argomenti posizionali devono venire prima degli argomenti con keyword

# Argomenti di default mutabili (cautela necessaria)
def addition(item, L=[]):
    L.append(item)
    return L

# Chiamate alla funzione 'addition'
print(addition('C')) # Output: ['C'], aggiunge 'C' alla lista L
print(addition('D')) # Output: ['C', 'D'], la lista L continua a crescere con gli elementi aggiunti
