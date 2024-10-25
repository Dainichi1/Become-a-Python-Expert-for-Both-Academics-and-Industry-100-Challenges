# Definizione della classe Rational per rappresentare i numeri razionali
class Rational:
    # Costruttore che prende il numeratore e il denominatore come input
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # Metodo per rappresentare il numero razionale come stringa
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    # Sovraccarico dell'operatore '+' per sommare due numeri razionali
    def __add__(self, other):
        # Calcolo del nuovo numeratore e denominatore
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        # Ritorna un nuovo oggetto Rational con il risultato della somma
        return Rational(new_numerator, new_denominator)

    # Sovraccarico dell'operatore '*' per moltiplicare due numeri razionali
    def __mul__(self, other):
        # Calcolo del nuovo numeratore e denominatore
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        # Ritorna un nuovo oggetto Rational con il risultato della moltiplicazione
        return Rational(new_numerator, new_denominator)

# Esempio di utilizzo della classe Rational con operator overloading
# Creazione di due numeri razionali
r1 = Rational(1, 2)  # 1/2
r2 = Rational(2, 3)  # 2/3

# Uso dell'operatore '+' sovraccaricato per sommare due numeri razionali
print("Somma:", r1 + r2)  # Output: Somma: 7/6

# Uso dell'operatore '*' sovraccaricato per moltiplicare due numeri razionali
print("Moltiplicazione:", r1 * r2)  # Output: Moltiplicazione: 2/6 o 1/3 se semplificato
