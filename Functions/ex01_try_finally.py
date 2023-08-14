FILENAME = 'ex01_data.txt'


def main():
    f = None

    try:

        try:
            f = open(FILENAME, 'w')
            print("file opened")
        except OSError:
            print("could not open the file for writing.")
            quit(1)
        else:
            print("enter numbers (ctrl + C to quit):")

            while True:
                num = int(input("number: "))
                f.write(f'{num}\n')

    except KeyboardInterrupt:
        print("user pressed CTRL + C")
    finally:

        if f is not None:
            print("closing file.")
            f.close()

if __name__ == '__main__':
    main()
