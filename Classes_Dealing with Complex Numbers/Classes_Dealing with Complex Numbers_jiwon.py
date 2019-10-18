import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real_ = self.real + no.real
        imaginary_ = self.imaginary + no.imaginary
        return Complex(real_, imaginary_)
        
    def __sub__(self, no):
        real_ = self.real - no.real
        imaginary_ = self.imaginary - no.imaginary
        return Complex(real_, imaginary_)
        
    def __mul__(self, no):
        real_ = (self.real * no.real) + (-1) * (self.imaginary * no.imaginary)
        imaginary_ = (self.real * no.imaginary) + (self.imaginary * no.real)
        return Complex(real_, imaginary_)

    def __truediv__(self, no):
        # (3 + 2i) / (2 + 1i) = (3 + 2i) * (1 / (2 + 1i))
        #                       (3 + 2i) * ((2 - 1i) / (2^2 + 1^2))
        real_ = (self.real * no.real) + (self.imaginary * no.imaginary)
        real_ = real_ / (no.real ** 2 + no.imaginary ** 2)
        imaginary_ = (-1) * (self.real * no.imaginary) + (self.imaginary * no.real)
        imaginary_ = imaginary_ / (no.real ** 2 + no.imaginary ** 2)
        return Complex(real_, imaginary_)

    def mod(self):
        real_ = (self.real ** 2 + self.imaginary ** 2) ** 0.5
        return Complex(real_, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result



if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
