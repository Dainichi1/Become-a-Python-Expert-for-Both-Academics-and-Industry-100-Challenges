from datetime import datetime, date, time, timedelta

# Ottenere la data e l'ora correnti
now = datetime.now()
print("Data e ora corrente:", now)  # Output: Data e ora corrente: YYYY-MM-DD HH:MM:SS

# Utilizzo della classe date per rappresentare solo la data
today = date.today()
print("Data odierna:", today)  # Output: Data odierna: YYYY-MM-DD

# Utilizzo della classe time per rappresentare solo l'ora
current_time = time(hour=12, minute=30, second=0)
print("Orario:", current_time)  # Output: Orario: 12:30:00

# Differenza tra due date e tempi con timedelta
d1 = datetime(2024, 10, 28, 12, 0, 0)
d2 = datetime(2024, 10, 29, 12, 0, 0)
difference = d2 - d1
print("Differenza di tempo:", difference)  # Output: Differenza di tempo: 1 day, 0:00:00

# Epoch time (1 gennaio 1970)
import time
epoch_time = time.time()
print("Tempo dall'epoch:", epoch_time)  # Output: Tempo dall'epoch: (secondi trascorsi dal 1 gennaio 1970)

# Ottenere l'ora locale strutturata
local_time = time.localtime()
print("Ora locale strutturata:", local_time)
print("Anno corrente:", local_time.tm_year)  # Output: Anno corrente: YYYY
print("Mese corrente:", local_time.tm_mon)   # Output: Mese corrente: MM

# Ottenere la data e l'ora in formato stringa
current_time_string = time.ctime()
print("Data e ora corrente in formato stringa:", current_time_string)  # Output: Data e ora corrente in formato stringa: Thu Oct 28 12:00:00 2024
