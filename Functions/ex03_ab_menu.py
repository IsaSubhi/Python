"""
this program manages two int variables: a & b
they are shown to the end-user followed by
a menu for changing them or saving/loading them
to a file
"""

# Globals
FILENAME = "ab_menu_data.txt"


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
            f = open(FILENAME, 'w')
            f.write(f'{a}\n{b}\n')
            f.close()
            print("data saved successfully")

        elif option == 'L':
            f = open(FILENAME)
            a = int(f.readline())
            b = int(f.readline())
            f.close()
            print("data loaded successfully")
        elif option == 'Q':
            keep_running = False

        else:
            print("Error: invalid option!")

    print("Goodbye")


if __name__ == '__main__':
    main()