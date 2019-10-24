import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary

    def __add__(self, no):
        add_real=self.real+no.real
        add_ima=self.imaginary+no.imaginary
        return Complex(add_real, add_ima)

    def __sub__(self, no):
        sub_real=self.real-no.real
        sub_ima=self.imaginary-no.imaginary
        return Complex(sub_real,sub_ima)

    def __mul__(self, no): #(a+bi)(c+di)=(ac-bd)+i(ad+bc)
        mul_real=self.real*no.real-self.imaginary*no.imaginary
        mul_ima=self.real*no.imaginary+self.imaginary*no.real
        return Complex(mul_real,mul_ima)

    def __truediv__(self, no):
        truediv_real=self.real*no.real+self.imaginary*no.imaginary
        truediv_ima=-1*self.real*no.imaginary+self.imaginary*no.real
        truediv_n=1.00/(no.real*no.real + no.imaginary*no.imaginary)
        return Complex(truediv_real*truediv_n,truediv_ima*truediv_n)


    def mod(self):
        mod_self= math.sqrt(self.real**2+self.imaginary**2)
        #return Complex(pow(self.real**2+self.imaginary**2, 0.5), 0)
        return Complex(mod_self, 0)


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
