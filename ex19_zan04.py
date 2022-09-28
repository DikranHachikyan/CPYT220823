
# print(f'name is:{__name__}')

if __name__ == '__main__':
    
    tpl = 11,12,34,56,77

    for item in enumerate(tpl, start=6):
        key, value = item
        print(f'key = {key} value = {value}')

    print('---')