# 1
# import time
# print(f'time:{time.time()}')

# 1.1
# import time as tm
# print(f'time:{tm.time()}')

# 2.
# from time import time, sleep 

# 2.2
# from time import time as now, sleep
# print(f'time:{now()}')

from time import time, sleep 
from functools import wraps


def to_upper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__original = func
        args = [ f'{v}'.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper    


if __name__ == '__main__':

    print('hello','python','c++','java','c')    

    print = to_upper(print)
    print('hello','python','c++','java','c')    

    print = print.__original
    print('hello','python','c++','java','c')    

    print('---')