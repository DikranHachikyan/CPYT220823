
def sort_priority(values, group):
    found = False
    def sort_helper(el):
        nonlocal found
        if el in group:
            found = True
            return (0,el)
        return (1,el)

    values.sort(key=sort_helper )
    return found

if __name__ == '__main__':
    
    numbers = [5, 4, 6, 3, 7, 9, 8]
    grp = {8,3,5}

    is_found = sort_priority(numbers, grp)

    print(f'numbers={numbers} is found:{is_found}')

    print('---')