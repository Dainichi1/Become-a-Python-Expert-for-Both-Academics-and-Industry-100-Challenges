from threading import Thread, Lock

# Definizione della classe MyData per sincronizzare l'accesso ai dati condivisi
class MyData:
    def __init__(self):
        self.data = 0            # Inizializzazione del dato condiviso
        self.flag = False         # Flag per coordinare producer e consumer
        self.lock = Lock()        # Creazione di un mutex (lock) per sincronizzare l'accesso

    # Metodo per inserire un dato (utilizzato dal producer)
    def put(self, d):
        # Attesa finché il flag non è False, cioè finché il consumer non ha letto il dato
        while self.flag != False:
            pass
        # Acquisizione del lock per evitare interferenze con il consumer
        self.lock.acquire()
        self.data = d             # Impostazione del nuovo dato
        self.flag = True          # Settaggio del flag a True per indicare che c'è un nuovo dato
        self.lock.release()       # Rilascio del lock per consentire l'accesso al consumer
        
    # Metodo per ottenere il dato (utilizzato dal consumer)
    def get(self):
        # Attesa finché il flag non è True, cioè finché il producer non ha prodotto un nuovo dato
        while self.flag != True:
            pass
        # Acquisizione del lock per evitare interferenze con il producer
        self.lock.acquire()
        x = self.data             # Lettura del dato
        self.flag = False         # Settaggio del flag a False per indicare che il dato è stato letto
        self.lock.release()       # Rilascio del lock per consentire l'accesso al producer
        return x                  # Ritorno del dato letto

# Funzione producer che genera dati e li inserisce in MyData
def producer(data):
    i = 1
    while True:
        data.put(i)               # Inserimento del dato in MyData
        print('Producer:', i)     # Stampa del dato prodotto
        i += 1                    # Incremento del dato da produrre

# Funzione consumer che legge i dati da MyData
def consumer(data):
    while True:
        x = data.get()            # Lettura del dato da MyData
        print('Consumer:', x)     # Stampa del dato consumato

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
