import gfx

while True:
    print("""
        1) Print a Line
        2) Print a Full Rectangle
        3) Print a Hollow Rectangle
        0) Quit
    """)

    option = input('enter option: ')

    match option:
        # print line
        case '1':
            char = input("what character to print? ")[0]
            length = int(input('what length of line? '))
            gfx.print_line(char, length)

        # print full rectangle
        case '2':
            w = int(input('what width? '))
            h = int(input('what height? '))
            gfx.print_rectangle(w, h)

        case '3':
            w = int(input('what width? '))
            h = int(input('what height? '))
            gfx.print_hollow_rectangle(w, h)

        case '0':
            break # break out of the menu while loop

        case _:
            print("Error: invalid option")

print("goodbye")