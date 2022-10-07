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


def to_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = [ f'{v}' for v in args]
        return func(*args, **kwargs)
    return wrapper

def add_brackets(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = [ f'[{v}]' for v in args]
        return func(*args, **kwargs)
    return wrapper

@add_brackets
@to_string
def concat(*args, **kwargs):
    '''Concatenate args with separator sep'''
    sep = kwargs.get('sep', ';')
    return sep.join(args)



if __name__ == '__main__':
    users = ['anna', 'maria', 'markus', 'jorg']

    print( concat(*users) )
    print( concat(*users, sep=',') )
    
    values = [11,23,45,6,77,3]
    print(concat(*values, sep='|'))
    print('---')