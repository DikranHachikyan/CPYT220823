def quit_app(*args):
    quit()  

if __name__ == '__main__':
    
    options = {
        '+': lambda a,b: a + b,
        'q': quit_app
    }
    
    n1 = float(input('n1='))
    n2 = float(input('n2='))
    ch = input('Action (+, q-quit):')

    if ch in '+q':
        res = options[ch](n1,n2)
        print(f'{n1} {ch} {n2} = {res}')

    print('---')