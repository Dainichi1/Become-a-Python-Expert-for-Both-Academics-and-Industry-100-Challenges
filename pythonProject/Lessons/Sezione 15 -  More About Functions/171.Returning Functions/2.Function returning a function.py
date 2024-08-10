def Outer():
    def display():
        print('Hello world')
    return display

d = Outer()
d()