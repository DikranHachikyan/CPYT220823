# %%
conn = dict(
    port=1521,
    host='localhost',
    db='northwind',
    keepalive=True
)

print(conn['host'])

# %%

user = {
    'phone': '111-22-33',
    'lastname' : 'Smith',
    'firstname':'Anna',
    'friends':['John', 'Markus'],
    'age': 36
}

print(user['lastname'])
print(user['friends'])

# %%

user1 = [ 'Anna', 'Smith', 36, '111-22-33']

# %%

user.keys()
# %%
user.values()
# %%

user.items()
# %%

'age' in user
# %%

user['email']

# %%

user.get('email', 'no@no.no')

# %%
