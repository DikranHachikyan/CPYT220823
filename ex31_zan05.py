# port - глобална променлива
port = 1521
# 1. дефиниция
def sum_numbers(a,b, *args):
    # тяло на функцията
    # c - локална променлива
    c = a + b
    print(f'args:{args} type:{type(args)}')
    for i in args:
        c += i 
    return c


if __name__ == '__main__':
    
    # 2. извикване
    res1 = sum_numbers(5,6)

    x,y,z = 10,20,5
    res2 = sum_numbers(x,y,z)

    arr = [1,2,3,4,5,6]

    res3 = sum_numbers(x,y, *arr)

    print(f'res1={res1} res2={res2} res3={res3}')

    print('---')