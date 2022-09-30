# port - глобална променлива

# 1. дефиниция
def show(title, *args, ver='1.0.3', size, **kwargs):

    print(f'positional, title:{title}')

    print(f'keyword-only arg, version:{ver}')
    print(f'keyword-only arg, size:{size}')

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

    show('Text Editor', *arr, ver='1.2.2', size=20)

    
    show('Text Editor', *arr, size=24)

    print('---')