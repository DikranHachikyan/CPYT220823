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


    p1.x = -10
    print(f'p1 x attr:{p1.x}')

    # Attribute Error
    # print(f'p2 x attr:{p2.x}')
    
    print('--- end ---')