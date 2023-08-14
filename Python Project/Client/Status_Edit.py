import os
from time import sleep

file_name = ''
exit_loop = False


def files_menu():
    global file_name
    global exit_loop
    while True:
        file = input("""Choose which file to edit:
    1) Status1.txt
    2) Status2.txt
    3) Status3.txt
    4) Enter file name
    5) Exit
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
                exit_loop = True
                break
            case _:
                print("No match found")
    if not exit_loop:
        print(f"Editing file {file_name}")
        sleep(1)
        file_edit()
    exit_loop = False


def file_edit():
    id_stat = ''
    alarm1 = ''
    alarm2 = ''
    while True:
        with open(file_name, 'r') as file:
            lines = []
            for line in file:
                lines.append(line.strip())
        while len(lines) < 3:  # if the file is missing arguments
            lines = []
            print("File is corrupted or is missing arguments. Please enter Station ID, Alarm 1 and Alarm 2")
            while not id_stat.isdigit() or len(id_stat) != 3:
                print("Station ID needs to consist of 3 integer")
                id_stat = input("Enter Station ID: ")
            while not (alarm1 == '0' or alarm1 == '1'):
                print("Alarm 1 needs to be 0 or 1")
                alarm1 = input("Enter Alarm 1: ")
            while not (alarm2 == '0' or alarm2 == '1'):
                print("Alarm 2 needs to be 0 or 1")
                alarm2 = input("Enter Alarm 2: ")
            with open(file_name, 'w') as file:
                file.write(f'{id_stat}\n{alarm1}\n{alarm2}')
                for i in id_stat, alarm1, alarm2:
                    lines.append(i)
        choose_edit = input("""Choose from:
    1) Edit Station ID
    2) Edit Alarm 1 status
    3) Edit Alarm 2 status
    4) Show file content
    5) Go Back
    6) Exit
    """)
        match choose_edit:
            case '1':
                id_stat = ''
                print(f"Current Station ID is: {lines[0]}")
                with open(file_name, 'w') as file:
                    while not id_stat.isdigit() or len(id_stat) != 3:
                        print("Station ID needs to consist of 3 integer")
                        id_stat = input("Enter new Station ID: ")
                    file.write(f'{id_stat}\n{lines[1]}\n{lines[2]}')
                    print("Station ID was updated")
            case '2':
                alarm1 = ''
                print(f"Current Alarm 1 status is: {lines[1]}")
                with open(file_name, 'w') as file:
                    while not (alarm1 == '0' or alarm1 == '1'):
                        print("Alarm 1 needs to be 0 or 1")
                        alarm1 = input("Enter new Alarm 1 status: ")
                    file.write(f'{lines[0]}\n{alarm1}\n{lines[2]}')
                    print("Alarm 1 was updated")
            case '3':
                alarm2 = ''
                print(f"Current Alarm 2 status is: {lines[2]}")
                with open(file_name, 'w') as file:
                    while not (alarm2 == '0' or alarm2 == '1'):
                        print("Alarm 2 needs to be 0 or 1")
                        alarm2 = input("Enter new Alarm 2 status: ")
                    file.write(f'{lines[0]}\n{lines[1]}\n{alarm2}')
                    print("Alarm 2 was updated")
            case '4':
                print(f"Station ID: {lines[0]}\nAlarm 1: {lines[1]}\nAlarm 2: {lines[2]}")
            case '5':
                files_menu()
                break
            case '6':
                break
            case _:
                print("No match found")
        sleep(1)


def main():
    files_menu()


if __name__ == '__main__':
    main()
