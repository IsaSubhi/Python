while True:

    width = int(input("enter width:"))
    height = int(input("enter height:"))

    # print header
    print('*' * width)

    if height > 1:
        # print center
        for row in range(height-2):
            if width > 1:
                print("*", end='')
                print(" " * (width-2), end='')
            print("*")

        # print footer
        print('*' * width)
