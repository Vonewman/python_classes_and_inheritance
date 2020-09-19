class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

point1 = Point(10, 100)
print(point1.getX())
