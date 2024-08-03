# Esempio di filter()
# La funzione filter() filtra gli elementi di un iterabile in base a una funzione fornita
def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

L = [3, 6, 7, 9, 12, 14, 19, 21]
f = filter(even, L)
for i in f:
    print(i)  # Output: 6, 12, 14

# Esempio di float()
# Converte un tipo di dato in float
print(float(12))  # Output: 12.0

# Esempio di format()
# Stessa funzionalità della formattazione delle stringhe
f = 12.34534
print(format(f, '0.2f'))  # Output: 12.35

# Esempio di frozenset()
# Converte un iterabile in un set immutabile
L = [1, 2, 3, 4, 5]
fs = frozenset(L)
print(fs)  # Output: frozenset({1, 2, 3, 4, 5})

# Esempio di globals()
# Restituisce tutte le variabili globali dichiarate all'interno di un programma Python
print(globals())

# Esempio di hasattr()
# Verifica se un oggetto ha un certo attributo
s1 = 'abcde'
print(hasattr(s1, 'lower'))  # Output: True

# Esempio di hash()
# Restituisce l'hash di un particolare oggetto
print(hash(s1))  # Output: Un valore hash per 'abcde'

# Esempio di help()
# Fornisce informazioni su un metodo o una classe
help(s1.lower)  # Output: Informazioni sulla funzione lower()

# Esempio di hex()
# Converte un numero in esadecimale
n = 10
print(hex(n))  # Output: 0xa

# Esempio di isinstance()
# Verifica se un oggetto è un'istanza di una particolare classe
print(isinstance(s1, str))  # Output: True

# Esempio di iter()
# Restituisce un iteratore per un dato iterabile
L = [10, 'john', 15.76, 'James']
itr = iter(L)
print(next(itr))  # Output: 10
print(next(itr))  # Output: 'john'

# Esempio di map()
# Applica una funzione a tutti gli elementi di un iterabile
L1 = [1, 2, 3, 4, 5]
L2 = [5, 6, 7, 8, 9]
m = map(lambda x, y: x + y, L1, L2)
print(list(m))  # Output: [6, 8, 10, 12, 14]

# Esempio di max(), min(), sum()
print(max(L1))  # Output: 5
print(min(L1))  # Output: 1
print(sum(L1))  # Output: 15

# Esempio di sorted()
print(sorted(L1))  # Output: [1, 2, 3, 4, 5]
print(sorted(L1, reverse=True))  # Output: [5, 4, 3, 2, 1]

# Esempio di slice()
s = slice(0, 2)
print(L2[s])  # Output: [5, 6]

# Esempio di zip()
L1 = ['A', 'B', 'C', 'D']
L2 = [2, 4, 6, 8]
z = zip(L1, L2)
for x, y in z:
    print(x, y)  # Output: A 2, B 4, C 6, D 8

# Esempio di reversed()
rev = reversed(L1)
print(next(rev))  # Output: 'D'

# Esempio di pow()
print(pow(2, 4))  # Output: 16

# Esempio di round()
print(round(12.3333))  # Output: 12
