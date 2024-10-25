from datetime import datetime

# Data e ora correnti
now = datetime.now()

# Convertire la data e l'ora in una stringa formattata usando strftime
data_ora_str = now.strftime("%d-%B-%Y %H:%M:%S")
print("Data e ora formattata:", data_ora_str)  # Output es: 25-October-2024 15:30:45

# Creare una stringa personalizzata con elementi specifici di data e ora
data_personalizzata = now.strftime("Oggi è %A, %d %B %Y, e sono le %H:%M")
print("Data personalizzata:", data_personalizzata)  # Output es: Oggi è Friday, 25 October 2024, e sono le 15:30

# Convertire una stringa in un oggetto datetime usando strptime
data_stringa = "28-10-2024 14:45:00"
data_oggetto = datetime.strptime(data_stringa, "%d-%m-%Y %H:%M:%S")
print("Oggetto datetime dalla stringa:", data_oggetto)  # Output: 2024-10-28 14:45:00
