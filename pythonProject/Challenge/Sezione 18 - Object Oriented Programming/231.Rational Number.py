class Rational:

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, other):
        p = self.p * other.q + self.q*other.p
        q = self.q * other.q
        sum = Rational(p,q)
        return sum

    def __sub__(self, other):
        p = self.p * other.q - self.q*other.p
        q = self.q * other.q
        sub = Rational(p,q)
        return sub

    def __str__(self):
        return str(self.p) + '/' + str(self.q)

i1 = Rational(2,3)
i2 = Rational(1,2)
i3 = i1+i2

print ('Sum of: ',i1," + ",i2," is: ",i3)