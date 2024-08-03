# Esempio 1: Variabile Globale e Variabile Locale con Nomi Diversi

x = 50  # Variabile globale

def func():
    y = 10  # Variabile locale
    print("Valore di x all'interno della funzione:", x)  # Accede alla variabile globale
    print("Valore di y all'interno della funzione:", y)  # Accede alla variabile locale

func()

print("Valore di x all'esterno della funzione:", x)

# Output:
# Valore di x all'interno della funzione: 50
# Valore di y all'interno della funzione: 10
# Valore di x all'esterno della funzione: 50


# Esempio 2: Variabile Locale con lo Stesso Nome di una Variabile Globale

x = 50  # Variabile globale

def func():
    x = 10  # Variabile locale (nasconde la variabile globale con lo stesso nome)
    print("Valore di x all'interno della funzione:", x)  # Stampa la variabile locale

func()

print("Valore di x all'esterno della funzione:", x)  # Stampa la variabile globale

# Output:
# Valore di x all'interno della funzione: 10
# Valore di x all'esterno della funzione: 50


# Esempio 3: Uso della Parola Chiave global per Modificare una Variabile Globale

x = 50  # Variabile globale

def func():
    global x  # Usa la parola chiave global per modificare la variabile globale
    x = 10  # Modifica la variabile globale
    print("Valore di x all'interno della funzione:", x)

func()

print("Valore di x all'esterno della funzione:", x)

# Output:
# Valore di x all'interno della funzione: 10
# Valore di x all'esterno della funzione: 10


# Esempio 4: Variabile Globale Modificata all'Interno di una Funzione Senza global

x = 50  # Variabile globale

def func():
    # x = x + 10  # Questo causerà un errore perché `x` locale è riferita prima di essere assegnata
    # print("Valore di x all' interno della funzione:", x)
    pass  # Commentato per evitare errore

# func()  # Decommenta per vedere l' errore

print("Valore di x all'esterno della funzione:", x)

# Output (se la funzione func() viene chiamata):
# UnboundLocalError: local variable 'x' referenced before assignment


# Esempio 5: Variabili Globali e Funzioni Annidate

def outer_func():
    x = 20  # Variabile locale per outer_func

    def inner_func():
        nonlocal x  # Usa la variabile `x` della funzione esterna
        x = 30  # Modifica la variabile `x` di outer_func
        print("Valore di x all' interno di inner_func:", x)

    inner_func()
    print("Valore di x all' interno di outer_func dopo inner_func:", x)

outer_func()

# Output:
# Valore di x all' interno di inner_func: 30
# Valore di x all' interno di outer_func dopo inner_func: 30


