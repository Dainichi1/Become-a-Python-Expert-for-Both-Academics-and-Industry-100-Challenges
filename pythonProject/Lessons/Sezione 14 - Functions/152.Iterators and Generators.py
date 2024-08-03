# Iteratori e generatori
# Gli iteratori permettono di iterare attraverso una sequenza di elementi
L = [1, 2, 3, 4, 5]
itr = iter(L)

# Uso della funzione next() per ottenere l' elemento successivo nella sequenza
print(next(itr))  # 1
print(next(itr))  # 2
print(next(itr))  # 3
print(next(itr))  # 4
print(next(itr))  # 5
# Se si chiama un' altra volta, lancerà StopIteration

# Possiamo scrivere i nostri iteratori chiamati GENERATORI che funzionano come iteratori
# Definizione di un generatore che ritorna i giorni della settimana in ciclo
def Days():
    L = ['Sun', 'Mon', 'Tue', 'Wed', 'Thru', 'Fri', 'Sat']
    i = 0
    while True:
        x = L[i]
        i = (i + 1) % 7
        yield x

d = Days()
# Stampa i giorni in sequenza e ritorna al primo una volta completata la settimana
print(next(d))  # Sun
print(next(d))  # Mon
print(next(d))  # Tue
print(next(d))  # Wed
print(next(d))  # Thru
print(next(d))  # Fri
print(next(d))  # Sat
print(next(d))  # Sun (ritorna al primo giorno)

# Nota: Il generatore non termina mai il ciclo, a meno che non venga interrotto manualmente