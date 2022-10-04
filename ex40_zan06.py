def foo(a=None, b=None):
    if not a: a = []
    if not b: b = {}

    print(f'a={a}')
    print(f'b={b}')

    print('-' * 30)
    n = len(a)
    a.append(n)
    b[n] = n
    

if __name__ == '__main__':
    
    foo()

    foo([4,2,6], {'Z':10})

    foo()
    
    foo([1,22,6,5], {'Z':10, 'X':11})

    foo()
    
    print('---')