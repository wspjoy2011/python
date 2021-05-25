class ComplexError(BaseException):
    def __init__(self, Complex, other):
        self.arg1 = Complex
        self.arg2 = other

class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
    def __str__(self):
        strRep = str(self.re)
        if self.im >= 0:
            strRep += '+'
        strRep += str(self.im) + 'i'
        return strRep
    def __add__(self, other):
        newRe = self.re + other.re
        newIm = self.im + other.im
        return Complex(newRe, newIm)
    def __mul__(self, other):
        if isinstance(other, Complex):
            newRe = self.re * other.re - self.im * other.im
            newIm = self.re * other.im + self.im * other.re
        elif isinstance(other, int) or isinstance(other, float):
            newRe = self.re * other
            newIm = self.im * other
        else:
            raise ComplexError(self, other)
        return Complex(newRe, newIm)
    __rmul__ = __mul__

a = Complex(1, 2)        
try:
    res = a * 'abcd'
except ComplexError as ce:
    print('Error in mul with args:', ce.arg1, ce.arg2)
