x = [ 'asd', '123', 'x32', '45', '44', '43', 'a', '22' ]
#       0       1     2     3      4     5   6     7    LEN: 8

# print all the elements of x that are convertible to int
# (isdigit -> true) and that are even

i = 0
while i < len(x):
    # fail test #1: check if it's not convertible to int:
    if not x[i].isdigit():
        i += 1
    else:
        num = int(x[i])

        # fail test #2: check if num's not even (if it's odd):
        if num % 2 != 0:
            i += 1
        else:
            print(num)
            i += 1
