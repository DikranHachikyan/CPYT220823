# 1. дефиниция на класа

class Point:
    
    def __init__(self, *, x=0, y=0, **kwargs):
        print('init point')
        # данни на обекта
        self.__x = x
        self.__y = y
    
    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.__x}, {self.__y})')

    def move_to(self, dx, dy):
        self.__x += dx
        self.__y += dy


if __name__ == '__main__':
    # 2. деклариране на променлива от типа
    # клас - типът, Point; обект - представител на класа, p
    print('--- begin ---')
    p1 = Point()
    p2 = Point(x=12, y=34)

    # p1.x = -10
    # 1. OK
    # print(f'point x={p1.x}')

    # 2. Ok
    # print(f'point x={p1._x}')

    # 3. AttributeError 'Point' object has no attribute '__x'
    # print(f'point x={p1.__x}')

    p1.draw()
    p2.draw()

    p1.move_to(30,40)
    p1.draw()
    
    print('--- end ---')