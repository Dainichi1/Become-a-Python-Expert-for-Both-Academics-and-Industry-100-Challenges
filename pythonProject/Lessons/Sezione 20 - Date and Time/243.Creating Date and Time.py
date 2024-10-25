from datetime import datetime, date, time

# Creazione di un oggetto datetime specificando data e ora
dt1 = datetime(2024, 10, 28, 15, 30, 0)  # Anno, Mese, Giorno, Ora, Minuti, Secondi
dt2 = datetime(2024, 11, 5, 10, 0, 0)

print("Data e ora dt1:", dt1)  # Output: Data e ora dt1: 2024-10-28 15:30:00
print("Data e ora dt2:", dt2)  # Output: Data e ora dt2: 2024-11-05 10:00:00

# Differenza tra due datetime
differenza = dt2 - dt1
print("Differenza tra dt2 e dt1:", differenza)  # Output: Differenza tra dt2 e dt1: X days, HH:MM:SS

# Confronto tra datetime
print("dt1 è maggiore di dt2?", dt1 > dt2)  # Output: False
print("dt1 è minore di dt2?", dt1 < dt2)    # Output: True

# Creazione di un oggetto date per rappresentare solo una data
data = date(2024, 10, 28)
print("Data:", data)  # Output: Data: 2024-10-28

# Creazione di un oggetto time per rappresentare solo l'ora
ora = time(15, 30, 0)  # Ora, Minuti, Secondi
print("Ora:", ora)  # Output: Ora: 15:30:00

# Confronto tra date
data1 = date(2024, 10, 28)
data2 = date(2024, 11, 5)
print("data1 è maggiore di data2?", data1 > data2)  # Output: False
print("data1 è minore di data2?", data1 < data2)    # Output: True
