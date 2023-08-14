# FUNCTIONS:
print("PROGRAM START")


def print_line(c, length, has_newline):
    print(c * length, end='')
    if has_newline:
        print()


def print_rectangle(width, height):
    for row in range(height):

        # print each column of the line
        print_line('*', width, False)

        # print a newline
        print()


# MAIN
w = 5
h = 3
print_rectangle(w, h)


