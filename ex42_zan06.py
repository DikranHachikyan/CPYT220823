  

if __name__ == '__main__':
    
    pow_xy = lambda x,y: x ** y

    z = pow_xy(2,4)
    print(f'z={z}')

    numbers = [4, 2, 6, 5, 8]

    for i in map(lambda el: el ** 2, numbers):
        print(f'i={i}')
    
    print('---')