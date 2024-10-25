
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info (self):
        print ('My name is: '+self.name+", My age is: "+str(self.age)+"")

    def make_sound(self):
        print ('miao')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info (self):
        print('My name is: ' + self.name + ", My age is: " + str(self.age) + "")

    def make_sound(self):
        print('bau')

def my_pet(pet):
    pet.info()
    pet.make_sound()

c = Cat('Pallino','2')
d = Dog ('Fido', '4')



my_pet(c)