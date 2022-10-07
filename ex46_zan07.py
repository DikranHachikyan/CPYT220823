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

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args,**kwargs)
        print(f'name: {func.__name__}, doc:{func.__doc__} time:{time()-t:.3f}')
    
    return wrapper


@measure_time
def foo(sleep_time=0.5):
    '''Function foo sleeps sleep_time seconds'''
    sleep(sleep_time)


if __name__ == '__main__':
    
    foo()
    foo(0.3)

    print(f'2 name:{foo.__name__}, doc:{foo.__doc__}')

    print('---')