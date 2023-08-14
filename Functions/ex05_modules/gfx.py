print("GFX MODULE LOAD START")

print("GFX __name__:", __name__)
def print_line(char, length, *, has_newline=True):
    # print(char * length, end='')
    #
    # if (has_newline):
    #     print()

    print(char * length, end='\n' if has_newline else '')

    # if (has_newline):
    #     end_value = '\n'
    # else:
    #     end_value = ''
    #
    # print(char * length, end=end_value)


def print_rectangle(width, height):
    for row in range(height):
        print_line('*', width)


def print_hollow_rectangle(width, height):
    for row in range(height):
        # print the characters of that row
        # character in the side prints as '*', in the middle prints as space
        for col in range(width):
            if row == 0 or row == height-1 or col == 0 or col == width-1:
                print('*', end='')
            else:
                print(' ', end='')
        # and the line of the current row and move to the next row
        print()



# print_line('~', 5)
#
# print_line('~', 5, has_newline=False)
# print()
#
# print_rectangle(7,8)
# print()
#
# print_hollow_rectangle(7,8)

print("GFX MODULE LOAD END")