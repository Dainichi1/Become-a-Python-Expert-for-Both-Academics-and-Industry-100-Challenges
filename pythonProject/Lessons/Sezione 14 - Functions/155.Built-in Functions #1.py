# abs() - Restituisce il valore assoluto di un numero
num = -10
print("Valore assoluto di -10:", abs(num))  # Output: 10

# ascii() - Restituisce una rappresentazione in formato stringa leggibile dei caratteri non ASCII
s = "Pythön"
print("ascii() su 'Pythön':", ascii(s))  # Output: 'Pyth\u00f6n'

# bin() - Converte un numero in una stringa binaria
n = 10
print("Binario di 10:", bin(n))  # Output: '0b1010'

# bool() - Converte un valore in tipo booleano
val = 0
print("Booleano di 0:", bool(val))  # Output: False

# bytearray() - Restituisce un array di byte, che è mutabile
b_array = bytearray([65, 66, 67])
print("Bytearray:", b_array)  # Output: bytearray(b'ABC')

# bytes() - Restituisce un oggetto byte, che è immutabile
b = bytes([65, 66, 67])
print("Bytes:", b)  # Output: b'ABC'

# callable() - Verifica se l' oggetto passato è chiamabile (come una funzione)
def func():
    return "Sono una funzione!"

print("func è chiamabile?:", callable(func))  # Output: True

# chr() - Restituisce il carattere corrispondente a un codice ASCII
print("Carattere ASCII 65:", chr(65))  # Output: 'A'

# complex() - Crea un numero complesso
c = complex(2, 3)
print("Numero complesso:", c)  # Output: (2+3j)

# dict() - Crea un dizionario
d = dict(a=1, b=2)
print("Dizionario:", d)  # Output: {'a': 1, 'b': 2}

# dir() - Restituisce una lista dei nomi definiti in un modulo
print("Nomi definiti nel modulo:", dir())  # Output: [elenco di nomi definiti in questo modulo]

# divmod() - Restituisce sia il quoziente che il resto come tuple
q, r = divmod(10, 3)
print("Quoziente e resto di 10 diviso 3:", q, r)  # Output: (3, 1)

# enumerate() - Restituisce una tupla contenente un indice e il valore corrispondente
seq = ['a', 'b', 'c']
print("Enumerate su ['a', 'b', 'c']:")
for index, value in enumerate(seq):
    print(f"Indice {index}: {value}")
# Output:
# Indice 0: a
# Indice 1: b
# Indice 2: c

# eval() - Valuta un' espressione data sotto forma di stringa
expr = "5 + 10"
print("Risultato di eval('5 + 10'):", eval(expr))  # Output: 15

# exec() - Esegue codice Python dinamicamente
exec("print('Hello, World!')")  # Output: Hello, World!
