# 1. дефиниция на класа

class Point:
    
    def __init__(self, *, x=0, y=0, **kwargs):
        print('init point')
        # данни на обекта
        self.x = x
        self.y = y
    
    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.x}, {self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy
    
    # методи за достъп до данните
    
    @property
    def x(self):
        # get method
        return self.__x
    
    @x.setter
    def x(self,x):
        # set method
        assert x >= 0 and x <= 1000, f'x must be between 0 and 1000'
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        assert y >= 0 and y <= 1000, f'y must be between 0 and 1000'
        self.__y = y


if __name__ == '__main__':
    # 2. деклариране на променлива от типа
    # клас - типът, Point; обект - представител на класа, p
    print('--- begin ---')
    
    p1 = Point(x=12, y=34)

    
    # p1.y = 10
    p1.y = 100
    p1.draw()
    p1.move_to(11,22)
    p1.draw()
    
    print('--- end ---')