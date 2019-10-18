class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        X = self.x - no.x
        Y = self.y - no.y
        Z = self.z - no.z
        return Points(X, Y, Z)

    def dot(self, no):
        T = self.x * no.x + self.y * no.y + self.z * no.z
        return T

    def cross(self, no):
        W1 = self.y * no.z - self.z * no.y
        W2 = self.x * no.z - self.z * no.x
        W3 = self.x * no.y - self.y * no.x
        return Points(W1, W2, W3)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
