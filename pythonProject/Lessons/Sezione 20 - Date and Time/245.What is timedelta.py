from datetime import datetime, timedelta

# Creazione di due oggetti datetime
dt1 = datetime(2010, 10, 20, 12, 0, 0)
dt2 = datetime(2011, 10, 20, 12, 0, 0)

# Calcolo della differenza tra dt2 e dt1 utilizzando timedelta
td = dt2 - dt1
print("Differenza di tempo:", td)  # Output: Differenza di tempo: 365 days, 0:00:00

# Accesso ai giorni e ai secondi nella differenza di tempo
print("Giorni:", td.days)          # Output: Giorni: 365
print("Secondi:", td.seconds)      # Output: Secondi: 0 (poiché la differenza è precisa a livello di giorni)

# Creazione di un periodo di tempo (durata) specifico usando timedelta
durata = timedelta(days=10, hours=5, minutes=30)
print("Durata specificata:", durata)  # Output: Durata specificata: 10 days, 5:30:00

# Aggiunta di un timedelta a un oggetto datetime
nuova_data = dt1 + durata
print("Nuova data dopo l'aggiunta della durata:", nuova_data)  # Output: Nuova data: 2010-10-30 17:30:00
