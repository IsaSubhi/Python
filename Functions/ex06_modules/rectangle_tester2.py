from gfx import print_hollow_rectangle as hr

# explicitly global
z = 100

def main():
    # x and y remain local
    x = 10
    y = 13
    hr(x, y)



if __name__ == '__main__':
    main()

