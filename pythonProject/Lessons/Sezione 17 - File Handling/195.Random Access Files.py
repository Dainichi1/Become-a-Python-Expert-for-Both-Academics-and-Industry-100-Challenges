# Apertura di un file binario in modalità lettura
with open('MyData.txt', 'rb') as file:
    # Posizione iniziale del puntatore del file (sarà 0 all'apertura)
    posizione_iniziale = file.tell()
    print(f"Posizione iniziale del puntatore: {posizione_iniziale}")

    # Lettura sequenziale del file (legge i valori uno per uno)
    primo_byte = file.read(1)
    print(f"Primo byte letto: {primo_byte}")

    # Usare il metodo seek() per spostare il puntatore a una posizione specifica
    file.seek(10)  # Sposta il puntatore al decimo byte del file
    posizione_attuale = file.tell()
    print(f"Posizione dopo seek(10): {posizione_attuale}")

    # Lettura di un byte alla posizione corrente
    byte_specifico = file.read(1)
    print(f"Byte specifico letto dopo seek(10): {byte_specifico}")

    # Spostare il puntatore di file rispetto alla posizione corrente
    file.seek(5, 1)  # Sposta il puntatore 5 byte avanti rispetto alla posizione corrente
    posizione_attuale = file.tell()
    print(f"Posizione dopo seek(5, 1): {posizione_attuale}")

    # Spostare il puntatore alla fine del file
    file.seek(-1, 2)  # Sposta il puntatore all'ultimo byte del file
    posizione_fine = file.tell()
    print(f"Posizione alla fine del file: {posizione_fine}")

    # Lettura dell'ultimo byte
    ultimo_byte = file.read(1)
    print(f"Ultimo byte letto: {ultimo_byte}")
