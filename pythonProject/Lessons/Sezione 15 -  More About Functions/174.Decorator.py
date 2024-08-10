def decorator(fun):
    def wrapper():
        print('*' * 10)
        fun()
        print('*' * 10)
    return wrapper

def display():
    print('Hello')


d = decorator(display)
d()

################################################

def decorator2(fun):
    def wrapper2(msg):
        print('*' * 10)
        fun(msg)
        print('*' * 10)
    return wrapper2

def display2(msg):
    print(msg)


d = decorator2(display2)
d('Welcome')

########################################################


def decorator3(fun):
    def wrapper3(msg):
        print('*' * 10)
        fun(msg)
        print('*' * 10)
    return wrapper3


@decorator3
def display3(msg):
    print(msg)



display3('Welcome')