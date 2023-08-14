import threading
import queue
import random
import time

def fuzz():
    time.sleep(random.randint(1, 3)/10)

def worker(num, q):
    while True:
        work = q.get()
        if work is None:
            q.put(None)
            break

        print("worker #{} doing work #{}".format(num, work))
        q.task_done()
        fuzz()



if __name__ == '__main__':
    print("MAIN THREAD START")

    work_queue = queue.Queue()

    for i in range(20):
        work_queue.put(i)

    workers = []
    for i in range(5):
        new_worker = threading.Thread(  target=worker, kwargs={'num':i, 'q':work_queue}  )
        workers.append(new_worker)
        new_worker.start()

    work_queue.join()
    work_queue.put(None)

    print("MAIN THREAD EXIT")






