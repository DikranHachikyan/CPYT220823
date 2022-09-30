# port - глобална променлива

# 1. дефиниция
def show(title, *, ver='1.0.3', size, **kwargs):

    print(f'positional, title:{title}')

    print(f'keyword-only arg, version:{ver}')
    print(f'keyword-only arg, size:{size}')
        
    print('kwargs')
    setts = {
        'col': kwargs.get('color', 'green'),
        'fnt': kwargs.get('font', 'sans-serif')
    }
    print(f'color:{setts["col"]} font:{setts["fnt"]}')
    print()

if __name__ == '__main__':
    
    # 2. извикване

    show('Text Editor', ver='1.2.2', size=20)

    
    show('Text Editor', size=24)

    print('---')