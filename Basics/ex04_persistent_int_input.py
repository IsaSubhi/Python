while True:
    try:
        num = int(input("enter an int:"))
        print(f"{num} * 10 = {num * 10}")
        break

    # if int() failed to convert input to int
    except ValueError:
        print("error: this is not an int")

    # if user pressed ctrl + c
    except KeyboardInterrupt:
        print("okay, goodbye")
        break


