x = "abcd hello world 123 hello !!!"
print(x)
x = x.replace('hello', 'goodbye')
print(x)

y = list(x) # convert str x to list of chars in y
y[2] = 'X' # change cell 2 ('c') to 'X'
del y[-3:] # delete cells -3 -2 -1 ("!!!")


x = ''.join(y)
print(x)


