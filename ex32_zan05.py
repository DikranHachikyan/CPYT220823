# port - глобална променлива

# 1. дефиниция
def show(title, ver='1.0.3', *args, **kwargs):

    print(f'positional, title:{title}')

    print(f'optional, version:{ver}')

    print('args:')
    for i in args:
        print(i, end=' ')
    if 'color' in kwargs and 'font' in kwargs:    
        print('kwargs')
        col = kwargs['color']
        fnt = kwargs['font']
        print(f'color:{col} font:{fnt}')
    print()

if __name__ == '__main__':
    
    # 2. извикване
    show('Text Editor')

    show('Text Editor', '1.2.2')

    show('Text Editor', '1.2.2', 1,2,3,4)

    show('Text Editor', '1.2.2', 1,2,3,4, font='monospace', color='red')

    print('---')