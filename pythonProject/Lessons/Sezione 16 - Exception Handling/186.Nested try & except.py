try:
    # Blocco di codice principale
    try:
    # Codice che potrebbe sollevare un'eccezione specifica
    except SpecificException as e:
# Gestione di una specifica eccezione
# Altri blocchi di codice che potrebbero sollevare altre eccezioni
except GeneralException as e:
# Gestione di un'eccezione generale


#####################################################################################
try:
    # Primo livello di try-except
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))

    try:
        # Secondo livello di try-except per la divisione
        result = num1 / num2
        print(f"The result is {result}")
    except ZeroDivisionError as e:
        # Gestione della divisione per zero
        print("Error: Cannot divide by zero.")

except ValueError as e:
    # Gestione dell'errore di input non valido
    print("Error: Invalid input, please enter numeric values.")
