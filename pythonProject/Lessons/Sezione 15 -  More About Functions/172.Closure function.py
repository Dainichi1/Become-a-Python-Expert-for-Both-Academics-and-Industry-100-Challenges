def Closure():
    msg = 'Hello'

    def display():
        print('*' * 10)
        print(msg)
        print('*' * 10)
    return display


d = Closure()
d()

##########################################

def Closure2(msg):

    def display():
        print('*' * 10)
        print(msg)
        print('*' * 10)
    return display


d = Closure2('Welcome')
d()