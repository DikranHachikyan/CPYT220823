# 1. дефиниция на класа

class Point:
    
    def __init__(self, *, x=0, y=0, visible=True, **kwargs):
        print('init point')
        # данни на обекта
        self.set_x(x)
        self.set_y(y)
        self.set_visible(visible)
    
    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.get_x()}, {self.get_y()})')

    def move_to(self, dx, dy):
        self.set_x( self.get_x() + dx)
        self.set_y( self.get_y() + dy)
    
    # методи за достъп до данните
    def set_x(self, x):
        assert x >= 0 and x <= 1000, f'x must be between 0 and 1000'
        self.__x = x

    def get_x(self):
        return self.__x

    def set_visible(self, visible):
        self.__visible = visible
    # get
    def is_visible(self):
        return self.__visible

    def set_y(self, y):
        assert y >= 0 and y <= 1000, f'y must be between 0 and 1000'
        self.__y = y

    def get_y(self):
        return self.__y

if __name__ == '__main__':
    # 2. деклариране на променлива от типа
    # клас - типът, Point; обект - представител на класа, p
    print('--- begin ---')
    
    p1 = Point(x=12, y=34)

    if p1.is_visible():
        p1.draw()

    # p1.set_y(10000)
    p1.set_y(100)
    p1.draw()
    p1.move_to(11,22)
    p1.draw()
    
    print('--- end ---')