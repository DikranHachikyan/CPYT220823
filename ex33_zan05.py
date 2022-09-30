# port - глобална променлива

# 1. дефиниция
def show(title, ver='1.0.3', *args, **kwargs):

    print(f'positional, title:{title}')

    print(f'optional, version:{ver}')

    print('args:')
    for i in args:
        print(i, end=' ')
    print()
        
    print('kwargs')
    setts = {
        'col': kwargs.get('color', 'green'),
        'fnt': kwargs.get('font', 'sans-serif')
    }
    print(f'color:{setts["col"]} font:{setts["fnt"]}')
    print()

if __name__ == '__main__':
    
    # 2. извикване
    arr = [1,2,3,4]

    show('Text Editor', '1.2.2', *arr)

    settings = {
        'font':'monospace',
        'bold':True, 
        'color':'red',
        'margins':[5,10,10,5]
    }

    show('Text Editor', '1.2.2', *arr, **settings )

    print('---')