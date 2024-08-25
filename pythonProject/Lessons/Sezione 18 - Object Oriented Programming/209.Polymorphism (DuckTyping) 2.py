def PetLover(pet):
    pet.talk()
    if hasattr(pet, 'walk'):
        pet.walk()

class Duck:
    def talk (self):
        print("Duck is talking")
    def walk (self):
        print ("Duck is walking")

class Dog:
    def talk (self):
        print("Dog is talking")
    

du = Duck()
PetLover(du)

do = Dog()
PetLover(do)