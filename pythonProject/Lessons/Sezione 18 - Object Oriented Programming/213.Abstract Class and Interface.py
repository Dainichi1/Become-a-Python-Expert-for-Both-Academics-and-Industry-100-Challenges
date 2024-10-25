# Importiamo ABC e abstractmethod dalla libreria abc
from abc import ABC, abstractmethod

# Definizione di una classe astratta che rappresenta un'interfaccia base
class Shape(ABC):
    # Metodo astratto obbligatorio per le classi figlie
    @abstractmethod
    def area(self):
        pass  # Definizione del metodo senza implementazione

    # Metodo concreto opzionale che può essere ereditato o sovrascritto
    def description(self):
        return "Questa è una forma geometrica."

# Definizione di una classe concreta che eredita da Shape e implementa il metodo area
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implementazione del metodo area per il rettangolo
    def area(self):
        return self.width * self.height

# Definizione di un'altra classe concreta che implementa il metodo area
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implementazione del metodo area per il cerchio
    def area(self):
        return 3.14159 * self.radius * self.radius

# Creazione delle istanze delle classi concrete
rectangle = Rectangle(5, 10)
circle = Circle(7)

# Utilizzo dei metodi area e description
print("Area del rettangolo:", rectangle.area())  # Output: Area del rettangolo: 50
print("Descrizione:", rectangle.description())   # Output: Questa è una forma geometrica
print("Area del cerchio:", circle.area())        # Output: Area del cerchio: circa 153.93804
