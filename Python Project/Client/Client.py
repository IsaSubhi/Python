import os
from time import sleep
import socket
import Status_Edit

file_name = "Status1.txt"
WAIT = 5
SERVER_ADDRESS = '127.0.0.1', 58877

file_change = input(f"Reading data from {file_name}, do you want to change the file? (Y)es / (N)o: ").lower()
if file_change == 'y' or file_change == 'yes':
    while True:
        file = input("""Choose from:
    1) Status1.txt
    2) Status2.txt
    3) Status3.txt
    4) Enter file name
    5) Edit Station
    6) Exit
        """)
        match file:
            case '1':
                file_name = "Status1.txt"
                break
            case '2':
                file_name = "Status2.txt"
                break
            case '3':
                file_name = "Status3.txt"
                break
            case '4':
                while True:
                    file_name = input("Enter file name: ").lower()
                    files_list = [x.lower() for x in os.listdir()]
                    if file_name not in files_list:
                        print("File doesn't exist in the directory")
                        continue
                    break
                break
            case '5':
                Status_Edit.main()
            case '6':
                exit()
            case _:
                print("No match found")
                sleep(1)
print(f"Reading from {file_name}")


def main():
    while True:
        with socket.socket() as s:
            s.connect(SERVER_ADDRESS)
            numbers = ''
            with open(file_name, 'r') as f:
                for line in f:
                    numbers = numbers + line.strip() + " "
            if numbers == '':
                s.send("Empty".encode())
                res = s.recv(1024).decode()
            else:
                s.send(numbers.encode())
                res = s.recv(1024).decode()
            print(res)
            s.close()
            sleep(WAIT)


if __name__ == '__main__':
    try:
        main()
    except ConnectionRefusedError:
        print("Could not connect to the server... \nShutting down")
    except ConnectionResetError:
        print("Connection was lost!")
    except KeyboardInterrupt:
        print("Connection was interrupted!")



