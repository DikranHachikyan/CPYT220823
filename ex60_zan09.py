# 1. дефиниция на класа

class Point:
    
    def __init__(self):
        print('init point')
        # данни на обекта
        self.x = 10
        self.y = 20
    
    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.x}, {self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy


if __name__ == '__main__':
    # 2. деклариране на променлива от типа
    # клас - типът, Point; обект - представител на класа, p
    print('--- begin ---')
    p = Point()

    print(f'type:{type(p)} point at ({p.x}, {p.y})')

    p.x = 15

    print(f'point ({p.x}, {p.y})') 
    
    p.draw()
    p.move_to(-16, 30)
    p.draw()
    
    print('--- end ---')