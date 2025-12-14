class Point:
    #Implement the class here
    count = 0

    @staticmethod
    def getter_count():
        return Point.count

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def y(self):
        Point.count += 1
        return self._y
    
    @property
    def x(self):
        Point.count += 1
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
    @y.setter
    def y(self, value):
        self._y = value

#Write test software under this if
if __name__ == "__main__":
    pass

