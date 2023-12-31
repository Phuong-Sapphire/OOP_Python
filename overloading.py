class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __gt__(self, other):
        return self.x > other.y and self.y > other.y


p1 = Point(1, 2)
p2 = Point(3, 5)

print(p1 + p2)
print(p1 > p2)
