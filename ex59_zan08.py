class NameNotFoundError(Exception):
    pass


def print_key(key, **kwargs):

    if key not in kwargs:    
        raise NameNotFoundError(f'Please, check ... {key}')

    print(f'{key} => {kwargs[key]}')
    print(f'--- end print_key {key}---')

if __name__ == '__main__':

    conn = {
        'host':'localhost',
        'port':1521,
        'service':'oracle'
    }
    try:
        print_key('host', **conn)
        print_key('ip', **conn)
    except NameNotFoundError as e:
        print(f'invalid key:{e}')
        
    print('---')