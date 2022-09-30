# port - глобална променлива
port = 1521
# 1. дефиниция
def sum_numbers(a,b,d=None):
    # тяло на функцията
    # c - локална променлива
    c = a + b + d if d else a + b 
    return c


if __name__ == '__main__':
    
    # 2. извикване
    res1 = sum_numbers(5,6)

    x,y,z = 10,20,5
    res2 = sum_numbers(x,y,z)

    print(f'res1={res1} res2={res2}')

    print('---')