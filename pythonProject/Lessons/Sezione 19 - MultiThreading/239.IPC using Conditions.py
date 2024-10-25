from threading import Thread, Condition
from time import sleep

# Definizione della classe MyData per sincronizzare l'accesso ai dati condivisi
class MyData:
    def __init__(self):
        self.data = 0                    # Inizializzazione del dato condiviso
        self.cv = Condition()             # Creazione di una variabile di condizione per la sincronizzazione

    # Metodo per inserire un dato (utilizzato dal producer)
    def put(self, d):
        # Acquisizione del lock e attesa della condizione
        self.cv.acquire()
        self.cv.wait(timeout=0)           # Il producer attende fino a quando viene notificato
        self.data = d                     # Impostazione del nuovo dato
        self.cv.notify()                  # Notifica al consumer che il dato è pronto
        self.cv.release()                 # Rilascio del lock
        sleep(1)                          # Simulazione di tempo di attesa

    # Metodo per ottenere il dato (utilizzato dal consumer)
    def get(self):
        # Acquisizione del lock e attesa della condizione
        self.cv.acquire()
        self.cv.wait(timeout=0)           # Il consumer attende fino a quando viene notificato
        x = self.data                     # Lettura del dato
        self.cv.notify()                  # Notifica al producer che il dato è stato letto
        self.cv.release()                 # Rilascio del lock
        sleep(1)                          # Simulazione di tempo di attesa
        return x                          # Ritorno del dato letto

# Funzione producer che genera dati e li inserisce in MyData
def producer(data):
    i = 1
    while True:
        data.put(i)                       # Inserimento del dato in MyData
        print('Producer:', i)             # Stampa del dato prodotto
        i += 1                            # Incremento del dato da produrre

# Funzione consumer che legge i dati da MyData
def consumer(data):
    while True:
        x = data.get()                    # Lettura del dato da MyData
        print('Consumer:', x)             # Stampa del dato consumato

# Creazione dell'istanza di MyData condivisa tra producer e consumer
data = MyData()

# Creazione e avvio dei thread per il producer e il consumer
t1 = Thread(target=lambda: producer(data))
t2 = Thread(target=lambda: consumer(data))

t1.start()
t2.start()

# Attesa che i thread finiscano (in questo caso non succede mai perché sono cicli infiniti)
t1.join()
t2.join()
