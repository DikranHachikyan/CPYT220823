# %%

arr = [12, 23, 45, 56, 67]

print(f'arr={arr} type:{type(arr)}')

# %%

print(id(arr))

arr[3] = 100

arr.append(20)

print(f'arr={arr} id={id(arr)}')

# %%

tp = 11,22,33,44,55

arr1 = list(tp)

print(f'arr1={arr1}')

# %%

s_arr = list('Hello Python')
print(s_arr)

# %%
