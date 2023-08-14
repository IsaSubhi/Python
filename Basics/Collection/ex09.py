x = [10, 20, 30]

print(F"x id:{id(x)} value:{x}")

# extends in place:
# x.extend( [11, 22, 33] )
x += [11, 22, 33]

print(F"x id:{id(x)} value:{x}")

# makes an extend copy:
x = x + [11, 22, 33]
print(F"x id:{id(x)} value:{x}")
