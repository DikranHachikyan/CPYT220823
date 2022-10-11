
if __name__ == '__main__':

    actions = {
        '+': lambda a,b: a + b
    }
    
    while True:
        try:
            op = input('action (+, q-quit):')
            if op == 'q':
                break
                # quit()
            value1 = float(input('first number:'))
            value2 = float(input('second number:'))
            result = actions[op](value1, value2)
        except (ValueError,KeyError) as e:
            print(f'Unsupported operation or invalid number:{e}')
        except Exception as e:
            print(f'Unknown error!{e}')
        else:
            print(f'{value1} {op} {value2} = {result}')
            continue
        finally:
            print('--- finally ---')



    print('---')