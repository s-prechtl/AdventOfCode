class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    start: Point
    end: Point
    axis: str

    def __init__(self, x1, y1, x2, y2):
        self.start = Point(x1, y1)
        self.end = Point(x2, y2)

        if x1 == x2:
            self.axis = "X"
        elif y1 == y2:
            self.axis = "Y"
        elif abs(x1 - x2) == abs(y1 - y2):
            self.axis = "DIAG"
        else:
            self.axis = "INVALID"
