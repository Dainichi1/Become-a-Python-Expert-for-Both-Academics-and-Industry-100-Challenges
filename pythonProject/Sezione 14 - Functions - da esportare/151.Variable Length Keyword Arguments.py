# Funzione che accetta un numero variabile di argomenti
def fun1(*args):
    print(args)

# Chiamate alla funzione con diversi argomenti
fun1(10, 8, 12, 9, 'John', 16)  # Output: (10, 8, 12, 9, 'John', 16)

# La funzione può essere chiamata anche con argomenti posizionali o keyword
def fun1(a, b, c):
    print(a, b, c)

fun1(10, 20, 15)                 # Output: 10 20 15
fun1(a=10, b=20, c=15)           # Output: 10 20 15

# Funzione che accetta un numero variabile di argomenti come keyword arguments
def fun2(**kwargs):
    print(kwargs)

# Chiamata alla funzione con keyword arguments
fun2(name='Ajay', roll=10, addr='Delhi')  # Output: {'name': 'Ajay', 'roll': 10, 'addr': 'Delhi'}

# Python permette di chiamare funzioni usando keyword arguments. Gli argomenti keyword devono seguire quelli posizionali.
# Gli argomenti keyword devono essere passati dopo gli argomenti posizionali.

# Funzione che accetta sia argomenti posizionali, argomenti a lunghezza variabile, che keyword arguments
def fun3(a, b, *args, **kwargs):
    print(a, b, args, kwargs)

# Chiamata alla funzione con vari tipi di argomenti
fun3(1, 2, 3, 4, 5, name='John', age=30)  # Output: 1 2 (3, 4, 5) {'name': 'John', 'age': 30}

# Funzione dove a e b devono essere posizionali, e c deve essere passato come keyword argument
def fun3(a, b, *args, c, **kwargs):
    print(a, b, c, args, kwargs)

# Chiamata alla funzione con argomenti misti
fun3(1, 2, 3, 4, 5, c=6, name='John', age=30)  # Output: 1 2 6 (3, 4, 5) {'name': 'John', 'age': 30}
