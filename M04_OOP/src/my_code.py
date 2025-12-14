import math

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

    @staticmethod
    def closest(p_list):
        if not p_list:
            raise ValueError("Point list is empty")

        min_distance = math.hypot(p_list[0]._x, p_list[0]._y)

        for p in p_list[1:]:
            dist = math.hypot(p._x, p._y)
            if dist < min_distance:
                min_distance = dist

        return min_distance

#Write test software under this if
if __name__ == "__main__":
    pass

