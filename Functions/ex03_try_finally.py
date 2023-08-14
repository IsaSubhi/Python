FILENAME = 'ex03_data.txt'


def main():
    f = None
    try:
        f = open(FILENAME, 'w')
        print("file opened")

        print("enter numbers (ctrl + C to quit):")

        while True:
            num = int(input("number: "))
            f.write(f'{num}\n')

    except OSError:
        print("could not open the file for writing.")
        quit(1)
    except KeyboardInterrupt:
        print("user pressed CTRL + C")
    finally:
        if f is not None:
            print("closing file.")
            f.close()

if __name__ == '__main__':
    try:
        main()
    except:
        print("something unexpected happend")
        raise
