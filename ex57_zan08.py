def print_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError as e:
        # 3. правилна обработка
        raise
        # 2. много лоша идея
        # pass

        # 1. не е добра идея
        # print(f'invalid key:{e}')
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
    except KeyError as e:
        print(f'invalid key:{e}')
        
    print('---')