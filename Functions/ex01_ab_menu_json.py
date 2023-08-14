"""
this program manages two int variables: a & b
they are shown to the end-user followed by
a menu for changing them or saving/loading them
to a file
"""
# Imports
import json

# Globals
FILENAME = "ab_menu_data.json"


def main():
    # initialize the data variables
    menu_data = {'a': 0, 'b': 0}

    # manages the menu loop
    keep_running = True

    # menu loop
    while keep_running:
        # print menu
        print(f'''A = {menu_data['a']},  B = {menu_data['b']}
        
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
            menu_data['a'] = int(input('enter a new value for A:'))

        elif option == 'B':
            menu_data['b'] = int(input('enter a new value for B:'))

        elif option == 'S':
            with open(FILENAME, 'w') as f:
                json.dump(menu_data, f)

            print("data saved successfully")

        elif option == 'L':
            with open(FILENAME) as f:
                menu_data = json.load(f)

            print("data loaded successfully")

        elif option == 'Q':
            keep_running = False

        else:
            print("Error: invalid option!")

    print("Goodbye")


if __name__ == '__main__':
    main()
