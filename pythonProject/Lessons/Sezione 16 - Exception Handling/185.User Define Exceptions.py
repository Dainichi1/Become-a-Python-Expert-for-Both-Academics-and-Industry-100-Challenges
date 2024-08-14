# Definire una nuova eccezione per età negativa
class NegativeAgeError(Exception):
    def __init__(self, age, message="Age cannot be negative"):
        self.age = age
        self.message = message
        super().__init__(self.message)

# Funzione per impostare l'età
def set_age(age):
    if age < 0:
        raise NegativeAgeError(age)
    return f"Age set to {age}"

try:
    age = int(input("Enter age: "))
    print(set_age(age))
except NegativeAgeError as e:
    print(f"Error: {e}")
