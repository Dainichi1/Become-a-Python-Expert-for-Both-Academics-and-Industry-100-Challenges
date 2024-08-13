L = [10, 20, 30, 40, 50]  # Lista di elementi

try:
    index = int(input('Enter an index: '))  # Richiede un indice all'utente
    print(L[index])  # Stampa l'elemento all'indice specificato
    print('End of try block')  # Indicando la fine del blocco try
except:
    print('Invalid index')  # Messaggio di errore generico
    print('Terminate gracefully')  # Messaggio che indica che il programma è terminato senza crash


############################################################################

L = [10, 20, 30, 40, 50]  # Lista di elementi

try:
    index = int(input('Enter an index: '))  # Richiede un indice all'utente
    print(L[index])  # Stampa l'elemento all'indice specificato
    print('End of try block')  # Indicando la fine del blocco try
except IndexError:
    print('Invalid index')  # Errore di indice non valido
except ValueError:
    print('Enter only integer value')  # Errore di tipo: solo valori interi sono accettati

print('Terminate gracefully')  # Messaggio che indica che il programma è terminato senza crash



#########################################################################################################
L = [10, 20, 30, 40, 50]  # Lista di elementi

try:
    index = int(input('Enter an index: '))  # Richiede un indice all'utente
    print(L[index])  # Stampa l'elemento all'indice specificato
    print('End of try block')  # Indicando la fine del blocco try
except (IndexError, ValueError) as msg:
    print(msg)  # Stampa il messaggio di errore
    print('Terminate gracefully')  # Messaggio che indica che il programma è terminato senza crash
