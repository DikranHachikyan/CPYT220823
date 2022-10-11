
if __name__ == '__main__':

    actions = {
        '+': lambda a,b: a + b
    }
    
    while True:
        try:
            op = input('action (+, q-quit):')
            if op == 'q':
                break
            value1 = float(input('first number:'))
            value2 = float(input('second number:'))
            result = actions[op](value1, value2)
        except KeyError as e:
            print(f'Unsupported operation:{e}')
        except ValueError as e:
            print(f'Invalid number:{e}')
        else:
            print(f'{value1} {op} {value2} = {result}')



    print('---')