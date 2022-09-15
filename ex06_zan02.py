# %%

tp = (12, 14, 34, 45, 67)

print(f'tp = {tp}')

# %%

print(tp[1])
# %%

# TypeError
# tp[1] = 120

# %%

a, b, c, d, e = tp

print(f'a={a}, b={b}, c={c}, d={d}, e={e}')
# %%

a, b, *_ = tp

print(f'a={a}, b={b}')

# %%

*_, a, b = tp

print(f'a={a}, b={b}')
# %%

tp = 11, 22, 33, 44, 55

print(f'tp={tp}')

# %%

t1 = (100,)

print(f't1={t1} type of t1:{type(t1)}')

# %%

33 in tp

# %%

5 not in tp

# %%

type(tp) is tuple

# %%
