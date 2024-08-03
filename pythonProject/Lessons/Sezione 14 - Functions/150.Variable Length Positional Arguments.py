# Funzione che accetta argomenti di lunghezza variabile (*args)
def fun1(*args):
    print(type(args), args)

# Esempi di chiamata della funzione con un numero variabile di argomenti
fun1()                 # Output: <class 'tuple'> ()
fun1(10, 20)           # Output: <class 'tuple'> (10, 20)
fun1(10, 20, 30, 40)   # Output: <class 'tuple'> (10, 20, 30, 40)

# Funzione che accetta argomenti posizionali e variabili (*args)
def fun1(a, b, *args):
    print(a, b, args)

# Esempi di chiamata della funzione con argomenti posizionali e variabili
fun1(11, 22)                   # Output: 11 22 ()
fun1(11, 22, 33, 44, 55)       # Output: 11 22 (33, 44, 55)

# Se una sequenza (lista, tupla, stringa) può essere passata come argomenti posizionali
def fun2(a, b, c):
    print(a, b, c)

s1 = 'sky'
fun2(*s1)  # Output: s k y

# Se una funzione restituisce più valori, è possibile scomporre questi valori in variabili diverse
def fun3(a, b, c):
    return a+1, b+1, c+1

x, y, z = fun3(10, 20, 30)
print(x, y, z)  # Output: 11 21 31
