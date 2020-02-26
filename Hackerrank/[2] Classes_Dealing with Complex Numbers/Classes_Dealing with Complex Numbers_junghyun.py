class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        R = self.real + no.real # R은 실수부
        I = self.imaginary + no.imaginary # I는 허수부
        return Complex(R,I)

    def __sub__(self, no):
        R = self.real - no.real
        I = self.imaginary - no.imaginary
        return Complex(R,I)

    def __mul__(self, no):
        R = (self.real * no.real) - (self.imaginary * no.imaginary)
        I = (self.real * no.imaginary) + (self.imaginary * no.real)
        return Complex(R,I)

    def __truediv__(self, no):
        T = math.pow(no.real,2) + math.pow(no.imaginary,2)
        # math.pow(a,n) 은 a의 n 제곱이라는 의미이다.
        R = (self.real * no.real + self.imaginary * no.imaginary) / T
        I = ((-1) * self.real * no.imaginary + self.imaginary * no.real) / T
        return Complex(R,I)

    def mod(self):
        T_1 = math.pow(self.real,2) + math.pow(self.imaginary,2)
        T_2 = math.sqrt(T_1)
        # math.sqrt(b) 은 루트 b 라는 의미이다.
        R = T_2
        I = 0
        return Complex(R,I)

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
