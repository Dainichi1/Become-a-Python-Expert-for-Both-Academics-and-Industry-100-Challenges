L = [10, 20, 30, 40, 50]  # Lista di elementi

try:
    index = int(input('Enter an index: '))  # Richiede un indice all'utente
    print(L[index])  # Stampa l'elemento all'indice specificato
    print('end of try block')
except IndexError:
    print('Invalid index')  # Messaggio di errore per indice non valido

print('Terminated gracefully')  # Messaggio di terminazione
