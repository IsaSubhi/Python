import socket
import sqlite3
import datetime

DB_PATH = 'data.sqlite3'
SERVER_ADDRESS = '127.0.0.1', 58877


class Table:  # unnecessary. For management purposes
    @staticmethod
    def create_table():  # creates the table if it doesn't exist
        with sqlite3.connect(DB_PATH) as conn:
            with conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS station_status (
                    station_id INTEGER PRIMARY KEY, 
                    last_date TEXT,
                    alarm1 INT,
                    alarm2 INT
                    );
                """)
                sock()

    @staticmethod
    def table_db(id_num, a1, a2):  # inserts data into database
        last_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        with sqlite3.connect(DB_PATH) as conn:
            with conn:
                conn.execute("""
                    INSERT OR REPLACE INTO station_status (station_id, last_date, alarm1, alarm2)
                    VALUES (?, ?, ?, ?);
                """, (id_num, last_date, a1, a2))
            cur = conn.execute("""
                 SELECT * FROM station_status
            """)
            all_data = cur.fetchall()
            if len(all_data) > 0:  # Checks if the table is empty
                print("----------------------------------")
                for id_num, last_date, a1, a2 in all_data:  # Can be deleted and enter "pass" instead
                    print(f'{id_num:03} {last_date:16} {a1:02} {a2:02}')
                print("----------------------------------")
                pass
            else:
                print("There is no data in the database")


def sock():
    with socket.socket() as s:
        s.bind(SERVER_ADDRESS)
        s.listen(5)
        print("listening...")
        client_socket, client_address = s.accept()
        message = client_socket.recv(1024).decode()
        print("Connected to:", client_address)
        if message == 'Empty':
            client_socket.send("No data was received".encode())
            print("No data was received")
        elif len(message.split()) != 3:
            client_socket.send("Missing required argument".encode())
            print("Missing required argument")
        else:
            message = message.split()
            if check_input(*message) == 1:
                client_socket.send("Station ID is corrupted!".encode())
                print("Station ID is corrupted!")
            elif check_input(*message) == 2:
                client_socket.send("Station alarm status is corrupted!".encode())
                print("Station alarm status is corrupted!")
            else:
                client_socket.send('Data was received'.encode())
                Table.table_db(*message)
    client_socket.close()


def check_input(in1, in2, in3):  # Checks that the received input is good
    if not in1.isdigit() or len(in1) != 3:
        return 1
    elif not (in2 == '0' or in2 == '1') or not (in3 == '0' or in3 == '1'):
        return 2
    else:
        pass


def main():
    Table.create_table()


if __name__ == '__main__':
    while True:
        try:
            main()
        except sqlite3.IntegrityError:
            print("Database mismatch!")
        except KeyboardInterrupt or ConnectionResetError:
            print("connection was forcefully closed!")
        except OSError:
            print("A connection is already established")
            break
        except TypeError:
            print("Missing required positional argument...\n Trying again...")
