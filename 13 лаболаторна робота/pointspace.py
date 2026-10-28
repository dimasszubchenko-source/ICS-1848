import math

class PointSpace:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def SetCoord(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def DisplayCoord(self):
        s = "({}, {}, {})".format(self.x, self.y, self.z)
        print(s)

    def Octant(self):
        # якщо точка лежить на координатній площині
        if self.x == 0 or self.y == 0 or self.z == 0:
            return 0
        if self.z > 0:
            if self.x > 0 and self.y > 0:
                return 1
            if self.x < 0 and self.y > 0:
                return 2
            if self.x < 0 and self.y < 0:
                return 3
            return 4
        else:
            if self.x > 0 and self.y > 0:
                return 5
            if self.x < 0 and self.y > 0:
                return 6
            if self.x < 0 and self.y < 0:
                return 7
            return 8

    def Dist(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
