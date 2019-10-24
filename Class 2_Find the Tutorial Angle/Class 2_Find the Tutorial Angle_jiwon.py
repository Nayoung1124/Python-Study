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
        return Points(x_, y_, z_)

    def dot(self, no):
        # 내적: (ax, ay)·(bx, by) = ax*ay + bx*by
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

    def cross(self, no):
        # 외적: A X B = (ax, ay, az) X (bx, by, bz))
        #            = (ay*bz-az*by, az*bx-ax*bz, ax*by-ay*bx)
        x_ = self.y * no.z - self.z * no.y
        y_ = self.z * no.x - self.x * no.z
        z_ = self.x * no.y - self.y * no.x
        return Points(x_, y_, z_)

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
