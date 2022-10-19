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
    # Специални методи
    # 
    # предефиниране на метод (function overriding)
    def __str__(self):
        return f'({self.x},{self.y})'

    def __eq__(self, other):
        # self.x - x на левия операнд (p1)
        # other.x - x на десния операнд (p2)
        if not isinstance(other, Point):
            raise NotImplementedError('Not yet implemented')
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        new_x, new_y = 0,0
        if isinstance(other,Point):
            new_x = self.x + other.x
            new_y = self.y + other.y
        elif isinstance(other, (float,int)):
            new_x = self.x + other
            new_y = self.y + other
        else:
            raise NotImplementedError('Not yet implemented')

        return Point(x=new_x, y=new_y)

    def __del__(self):
        print(f'destroy object:{self}')

def show():
    p = Point()
    print(f'show:{p}')

if __name__ == '__main__':
    # 2. деклариране на променлива от типа
    # клас - типът, Point; обект - представител на класа, p
    print('--- begin ---')
    
    p1 = Point(x=12, y=34)
    p2 = Point(x=12, y=34)
    
    print(f'p1:{p1}')
    # p3 = p1

    if p1 == p2:
        print(f'{p1} = {p2}')
    else:
        print(f'{p1} <> {p2}')

    p3 = p1 + p2
    print(f'p3:{p3}')
    del p3

    p1 = p1 + 20.5
    print(f'p1:{p1}')

    show()
    print('--- end ---')