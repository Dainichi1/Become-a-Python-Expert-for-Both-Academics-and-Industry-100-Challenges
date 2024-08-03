# Funzione filter()
# La funzione filter() filtra oggetti da un iterabile in base a una funzione che fornisci

L = [3, 6, 7, 9, 12, 14, 19, 21]

# Definisco una funzione che restituisce True per numeri pari
def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

# Uso filter() per ottenere solo i numeri pari dalla lista
f = filter(even, L)

# Stampo gli elementi filtrati
for i in f:
    print(i)  # Output: 6, 12, 14


# Funzione float()
# Converte un tipo di dato in float
n = 12.345
f = float(n)
print(f)  # Output: 12.345


# Funzione format()
# Usata per formattare le stringhe in modo simile alla formattazione delle stringhe
formatted_string = "{:.2f}".format(n)
print(formatted_string)  # Output: 12.35


# Funzione frozenset()
# Converte qualsiasi oggetto iterabile in un set immutabile
S = [1, 2, 3, 4, 5]
frozen_S = frozenset(S)
print(frozen_S)  # Output: frozenset({1, 2, 3, 4, 5})


# Funzione globals()
# Restituisce tutte le variabili globali dichiarate all'interno di un programma Python
g = globals()
print(g)


# Funzione hasattr()
# Verifica se un oggetto ha un determinato attributo
s1 = 'abcde'
print(hasattr(s1, 'lower'))  # Output: True
print(hasattr(s1, 'isdigit'))  # Output: False


# Funzione hash()
# Restituisce il valore hash di un oggetto
print(hash(s1))  # Output: (un numero intero che rappresenta l'hash)
n = 10
print(hash(n))  # Output: 10
f = 12.345
print(hash(f))  # Output: 795515838178725900


# Funzione help()
# Fornisce dettagli su qualsiasi metodo o classe
help(s1.lower)  # Output: Help on built-in function lower
help(s1.isdigit)  # Output: Help on built-in function isdigit


# Funzione hex()
# Converte un numero in formato esadecimale
n = 255
print(hex(n))  # Output: 0xff


# Funzione isinstance()
# Controlla se un oggetto è un'istanza di una determinata classe
s1 = 'abcde'
n = 10
f = 12.34
print(isinstance(s1, str))  # Output: True
print(isinstance(n, int))  # Output: True
print(isinstance(f, float))  # Output: True


# Funzione issubclass()
# Controlla se una classe è una sottoclasse di un'altra
class A: pass
class B(A): pass

print(issubclass(B, A))  # Output: True
print(issubclass(A, B))  # Output: False


# Funzione iter()
# Aiuta a iterare su ogni elemento in una sequenza utilizzata insieme a next()
L = [10, 'john', 15.76, 'James']
itr = iter(L)
print(next(itr))  # Output: 10
print(next(itr))  # Output: 'john'
print(next(itr))  # Output: 15.76
print(next(itr))  # Output: 'James'
