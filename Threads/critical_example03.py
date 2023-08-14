import threading
import time
import random

people = [
    ('Moshe', 'Levi'),
    ('David', 'Cohen'),
    ('Shlomo', 'Azulai'),
    ('Lea', 'Aharonovich')
]

# critical section data
chosen_fname = "FNAME"
chosen_lname = "LNAME"
# lock for the data  above
chosen_lock = threading.Lock()

def fuzz():
    time.sleep(random.randint(1, 3)/10)

def update_chosen():
    global chosen_fname, chosen_lname

    #while True:
    for i in range(10000):
        for person in people:
            fuzz()

            with chosen_lock:
                fuzz()
                chosen_fname = person[0]
                fuzz()
                chosen_lname = person[1]



def print_chosen():
    #while True:
    for i in range(10000):
        fuzz()
        with chosen_lock:
            fuzz()
            fname = chosen_fname
            fuzz()
            lname = chosen_lname
            fuzz()


        print(fname, lname, 'OK' if ((fname,lname) in people) else 'ERROR')


update_thread = threading.Thread(target=update_chosen)
print_thread = threading.Thread(target=print_chosen)

update_thread.start()
print_thread.start()


update_thread.join()
print_thread.join()
print("MAIN THREAD EXIT")