x = [ 'asd', '123', 'x32', '45', '44', '43', 'a', '22' ]
#       0       1     2     3      4     5   6     7    LEN: 8

# print all the elements of x that are convertible to int
# (isdigit -> true) and that are even

i = 0
while i < len(x):
    # check if it's convertible to int:
    if x[i].isdigit():
        num = int(x[i])

        # check if num's is even:
        if num % 2 == 0:
            print(num)

    i += 1

# != --> ==
#  < --> >=
#  > --> <=