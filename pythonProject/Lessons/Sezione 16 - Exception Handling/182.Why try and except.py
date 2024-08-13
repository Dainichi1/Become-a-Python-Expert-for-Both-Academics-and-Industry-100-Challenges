def div(a, b):
    if b != 0:
        return a // b  # Uso della divisione intera
    else:
        return -1  # Codice di errore per la divisione per zero

# Prendere input dall'utente
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

c = div(a, b)

if c == -1:
    print('Zero division error')
else:
    print(c)


####################################################################

def div(a, b):
    if b != 0:
        return a // b
    else:
        raise ZeroDivisionError  # Lancia un'eccezione personalizzata

# Prendere input dall'utente
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

try:
    c = div(a, b)
    print(c)
except ZeroDivisionError:
    print('Zero division error')
