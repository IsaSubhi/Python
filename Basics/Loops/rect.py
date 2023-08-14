while True:

    width = int(input("enter width:"))
    height = int(input("enter height:"))

    for row in range(height):

        # print each column of the line
        for col in range(width):
            print('*', end='')

        # print a newline
        print()
