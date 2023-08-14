x = ['asd', '123', 'x32', '45', '44', '43', 'a', '22']
#       0       1     2     3      4     5   6     7    LEN: 8

# print all the elements of x that are convertible to int
# (isdigit -> true) and that are even

for text in x:
    # fail test #1: check if it's not convertible to int:
    if not text.isdigit():
        continue

    num = int(text)

    # fail test #2: check if num's not even (if it's odd):
    if num % 2 != 0:
        continue

    print(num)
