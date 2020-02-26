import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        x_ = self.x - no.x
        y_ = self.y - no.y
        z_ = self.z - no.z
        return Points(x_,y_,z_)

    def dot(self, no):
        x_dot = self.x*no.x
        y_dot = self.y*no.y
        z_dot = self.z*no.z
        sum_dot = x_dot+y_dot+z_dot
        return sum_dot
        
    def cross(self, no):
        cro_1 = self.y*no.z - self.z*no.y 
        cro_2 = self.z*no.x - self.x*no.z
        cro_3 = self.x*no.y - self.y*no.x
        return Points(cro_1, cro_2, cro_3)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
