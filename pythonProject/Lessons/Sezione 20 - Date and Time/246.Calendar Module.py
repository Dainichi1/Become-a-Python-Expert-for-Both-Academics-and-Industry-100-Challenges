import calendar

# Creazione di un calendario di testo per un mese specifico
anno = 2024
mese = 10
calendario_mensile = calendar.month(anno, mese)
print("Calendario di ottobre 2024:")
print(calendario_mensile)

# Creazione di un calendario di testo per un anno specifico
calendario_annuale = calendar.calendar(anno)
print("Calendario del 2024:")
print(calendario_annuale)

# Verifica se un anno è bisestile
anno_bisestile = 2024
print(f"L'anno {anno_bisestile} è bisestile?", calendar.isleap(anno_bisestile))  # Output: True

# Conteggio degli anni bisestili tra due anni
start_year = 2000
end_year = 2024
numero_bisestili = calendar.leapdays(start_year, end_year)
print(f"Anni bisestili tra {start_year} e {end_year}:", numero_bisestili)

# Ottenere il primo giorno del mese e il numero di giorni del mese
primo_giorno, num_giorni = calendar.monthrange(anno, mese)
print("Primo giorno del mese (0=Lunedì):", primo_giorno)  # Output: giorno della settimana (0=Lunedì)
print("Numero di giorni in ottobre 2024:", num_giorni)
