
def foo(values, n):
    n = n ** 2
    print(f'n={n}')

    values.sort()

if __name__ == '__main__':
    
    numbers = [5, 4, 6, 3, 7, 9, 8]
    a = 10

    foo(numbers, a)
    
    print(f'numbers={numbers} a={a}')
    print('---')