while True:

    width = int(input("enter width:"))
    height = int(input("enter height:"))

    for row in range(height):

        # print each column of the line
        for col in range(width):
            # check if in edge
            if (row == 0 or row == height-1 or
                    col == 0 or col == width-1):
                print('* ', end='')
            else:
                print('  ', end='')

        # print a newline
        print()
