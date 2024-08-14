try:
    # Codice che potrebbe generare un'eccezione
    pass
except ExceptionType:
    # Codice che gestisce l'eccezione
    pass
else:
    # Codice che viene eseguito solo se il blocco try non solleva eccezioni
    pass




########################################################################################
print('Before try')

try:
    a = int(input('Enter numerator: '))
    b = int(input('Enter denominator: '))
    c = a // b
    print('Try Block executed successfully')
except ZeroDivisionError as err:
    print(err)  # Gestione dell'errore di divisione per zero
else:
    print('Division is', c)  # Questo viene eseguito solo se non ci sono eccezioni

print('Outside try-except-else')
