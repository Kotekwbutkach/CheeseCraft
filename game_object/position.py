class Position:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y
        raise IndexError(f"No index {item} to get in Position object")

    def __setitem__(self, item, value):
        if item == 0:
            self.x = value
            return self
        if item == 1:
            self.y = value
            return self
        raise IndexError(f"No index {item} to set in Position object")

    def __add__(self, other):
        return Position(self[0] + other[0], self[1] + other[1])

