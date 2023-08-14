

for row in range(1, 11):
    # print each column print it
    for col in range(1, 11):
        print("{:3} ".format(row * col), end="")
    # after printing the entire line, go down
    print()

