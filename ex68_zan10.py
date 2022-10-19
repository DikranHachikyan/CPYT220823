
from draw import Point

def show():
    p = Point()
    print(f'show:{p}')

if __name__ == '__main__':
    # 2. деклариране на променлива от типа
    # клас - типът, Point; обект - представител на класа, p
    print('--- begin ---')
    
    p1 = Point(x=12, y=34)
    p2 = Point()
    p3 = Point()
    
    print(f'p1:{p1} count:{Point.count}')
    p1.draw()

    print('--- end ---')