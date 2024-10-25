class Robot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print ('Hello, my name is: '+self.name)


class PoliceRobot(Robot):

    def say_hi(self):
        print('Hello, my name is: '+self.name+' and I am a police robot')


r1 = Robot('Prova')
r1.say_hi()

r2 = PoliceRobot('Prova2')
r2.say_hi()
