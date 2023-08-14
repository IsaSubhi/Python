# FUNCTIONS:
# print("PROGRAM START")


def print_rectangle(width, height):
    for row in range(height):

        # print each column of the line
        for col in range(width):
            print('*', end='', flush=True)

        # print a newline
        print()


# MAIN
print("example1:")
print_rectangle(12, 7)
print("example2:")
print_rectangle(5, 3)
print("example3:")

w = int(input("w:"))
h = int(input("h:"))
print_rectangle(w, h)

print("PROGRAM END")
