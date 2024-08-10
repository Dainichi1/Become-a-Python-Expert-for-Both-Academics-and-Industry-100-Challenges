def Outer():
    def Inner():
        print ('I am an inner Function')
    Inner()

Outer()