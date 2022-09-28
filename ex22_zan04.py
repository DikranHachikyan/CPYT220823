
# print(f'name is:{__name__}')

if __name__ == '__main__':
    
    users = ['anna','maria','markus','jorg', 'florian']
    emails = [
        'anna@no.com',
        'maria@no.com',
        'markus@no.com',
        'jorg@no.com'
    ]

    for data in zip(users, emails):
        name, mail = data
        print(f'data={data} name={name} =>{mail}')


    print('---')