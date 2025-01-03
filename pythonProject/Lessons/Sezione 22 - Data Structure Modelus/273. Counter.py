from collections import Counter

# Creazione di un Counter a partire da una lista
L = ['Mark', 'Jonny', 'David', 'Mark', 'Jonny', 'Mark', 'James', 'Mathew']
c = Counter(L)

# Stampa il Counter, che conta le occorrenze di ciascun elemento
print(c)  # Output: Counter({'Mark': 3, 'Jonny': 2, 'David': 1, 'James': 1, 'Mathew': 1})

# Accesso al conteggio di un elemento specifico
print(c['Mark'])  # Output: 3 (numero di volte che 'Mark' appare nella lista)

# keys(): Restituisce tutte le chiavi (elementi del Counter)
print(c.keys())  # Output: dict_keys(['Mark', 'Jonny', 'David', 'James', 'Mathew'])

# values(): Restituisce tutti i valori (conteggi degli elementi)
print(c.values())  # Output: dict_values([3, 2, 1, 1, 1])

# items(): Restituisce tutte le coppie chiave-valore (elementi e conteggi)
print(c.items())  # Output: dict_items([('Mark', 3), ('Jonny', 2), ('David', 1), ('James', 1), ('Mathew', 1)])

# update(): Aggiorna il Counter aggiungendo nuovi elementi o incrementando i conteggi esistenti
c.update({'Marco': 4})  # Aggiunge 'Marco' con conteggio 4
print(c)  # Output: Counter({'Mark': 3, 'Marco': 4, 'Jonny': 2, 'David': 1, 'James': 1, 'Mathew': 1})

# get(): Restituisce il conteggio di un elemento specifico (o 0 se non esiste)
print(c.get('Mark'))  # Output: 3
print(c.get('NonExistent'))  # Output: 0

# copy(): Crea una copia del Counter
c_copy = c.copy()
print(c_copy)  # Output: Counter({'Mark': 3, 'Marco': 4, 'Jonny': 2, 'David': 1, 'James': 1, 'Mathew': 1})

# clear(): Rimuove tutti gli elementi dal Counter
c_copy.clear()
print(c_copy)  # Output: Counter()

# elements(): Restituisce tutti gli elementi, ripetuti in base al loro conteggio
for i in c.elements():
    print(i, end=" ")  # Output: Mark Mark Mark Jonny Jonny David James Mathew Marco Marco Marco Marco
print()

# pop(): Rimuove un elemento specifico dal Counter e restituisce il suo conteggio
removed_count = c.pop("Marco")  # Rimuove 'Marco'
print(removed_count)  # Output: 4
print(c)  # Output: Counter({'Mark': 3, 'Jonny': 2, 'David': 1, 'James': 1, 'Mathew': 1})

# popitem(): Rimuove e restituisce una coppia chiave-valore casuale
popped_item = c.popitem()
print(popped_item)  # Output: ('Mathew', 1) (o altro elemento casuale)
print(c)  # Output: Counter({'Mark': 3, 'Jonny': 2, 'David': 1, 'James': 1}) (senza l'elemento rimosso)

# most_common(): Restituisce una lista degli elementi più comuni (in ordine decrescente di conteggio)
print(c.most_common(1))  # Output: [('Mark', 3)] (elemento più comune con il suo conteggio)
print(c.most_common(2))  # Output: [('Mark', 3), ('Jonny', 2)] (2 elementi più comuni)

# Aggiunta di un nuovo aggiornamento per completare il Counter
c.update(['Mark', 'Jonny', 'David'])
print(c)  # Output: Counter({'Mark': 4, 'Jonny': 3, 'David': 2, 'James': 1})

