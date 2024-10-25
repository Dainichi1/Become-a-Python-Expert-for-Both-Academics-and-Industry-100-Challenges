from threading import Thread, Condition
from time import sleep
from queue import *

q = Queue()

# Funzione producer che genera dati e li inserisce in MyData
def producer(queu):
    i = 1
    while True:
        queu.put(i)                       # Inserimento del dato in MyData
        print('Producer:', i)             # Stampa del dato prodotto
        i += 1                            # Incremento del dato da produrre

# Funzione consumer che legge i dati da MyData
def consumer(queu):
    while True:
        x = queu.get()                    # Lettura del dato da MyData
        print('Consumer:', x)             # Stampa del dato consumato



# Creazione e avvio dei thread per il producer e il consumer
t1 = Thread(target=lambda: producer(q))
t2 = Thread(target=lambda: consumer(q))

t1.start()
t2.start()

# Attesa che i thread finiscano (in questo caso non succede mai perché sono cicli infiniti)
t1.join()
t2.join()
