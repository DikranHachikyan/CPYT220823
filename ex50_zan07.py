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


@to_upper
def concat(*args, **kwargs):
    '''Concatenate args with separator sep'''
    sep = kwargs.get('sep', ';')
    return sep.join(args)



if __name__ == '__main__':
    users = ['anna', 'maria', 'markus', 'jorg']
    values = [11,23,45,6,77,3]

    print(concat(*users))
    print(concat(*values, sep='/'))
    
    print(concat.__original(*users))
    concat = concat.__original
    print(concat(*users))

    print('---')