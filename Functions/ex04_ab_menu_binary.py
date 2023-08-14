"""
this program manages two int variables: a & b
they are shown to the end-user followed by
a menu for changing them or saving/loading them
to a file
"""

# Globals
FILENAME = "ab_little.bin"
ORDER = 'little'  # endianess of data saved/loaded
SIZE = 4  # how many bytes per number to save/load


def main():
    # initialize the data variables
    a = 0
    b = 0

    # manages the menu loop
    keep_running = True

    # menu loop
    while keep_running:
        # print menu
        print(f'''A = {a},  B = {b}
        
        set (A)
        set (B)
        (S)ave
        (L)oad
        (Q)uit        
        ''')

        # get option
        option = input("enter option:").upper()

        # resolve option
        if option == 'A':
            a = int(input('enter a new value for A:'))

        elif option == 'B':
            b = int(input('enter a new value for B:'))

        elif option == 'S':
            with open(FILENAME, 'wb') as f:
                data = a.to_bytes(SIZE, ORDER)
                f.write(data)

                f.write(b.to_bytes(SIZE, ORDER))

            print("data saved successfully")

        elif option == 'L':
            with open(FILENAME, 'rb') as f:
                # data = f.read(SIZE)
                # a = int.from_bytes(data, ORDER)
                #
                # b = int.from_bytes(f.read(SIZE), ORDER)

                data = f.read()
                a = int.from_bytes(data[:SIZE], ORDER)
                b = int.from_bytes(data[SIZE:], ORDER)



            print("data loaded successfully")
        elif option == 'Q':
            keep_running = False

        else:
            print("Error: invalid option!")

    print("Goodbye")


if __name__ == '__main__':
    main()