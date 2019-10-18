import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        s_real = self.real + no.real
        s_imaginary = self.imaginary + no.imaginary
        return Complex(s_real,s_imaginary)
    def __sub__(self, no):
        s_real = self.real - no.real
        s_imaginary = self.imaginary - no.imaginary
        return Complex(s_real,s_imaginary)       
    def __mul__(self, no):
        s_real = self.real*no.real - self.imaginary*no.imaginary
        s_imaginary = self.real*no.imaginary + self.imaginary*no.real
        return Complex(s_real,s_imaginary)

    def __truediv__(self, no):
        s_real = (self.real*no.real + self.imaginary*no.imaginary)/(no.real*no.real+no.imaginary*no.imaginary)
        s_imaginary = (-self.real*no.imaginary + self.imaginary*no.real)/(no.real*no.real+no.imaginary*no.imaginary)
        return Complex(s_real,s_imaginary)

    def mod(self):
        pmod=self.real*self.real + self.imaginary*self.imaginary
        mod_ = math.sqrt(pmod) #math모듈을 이용한 루트 함수
        return Complex(mod_,0.00)

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
