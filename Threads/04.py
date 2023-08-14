'''
Created on Nov 4, 2015

@author: rte
'''

import threading,time

class myThread(threading.Thread):
    def __init__(self,threadID, name, delayTime):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delayTime = delayTime
    def run(self):
        print("Starting: " + self.name)
        # Lock To Synchronize The Threads
        threadLock.acquire()
        print(threading.currentThread())
        printFunction(self.name,self.delayTime,3)
        # Unlock To Release The Next Thread
        threadLock.release()

def printFunction(threadName, delayTime, counter):
    while counter:
        time.sleep(delayTime)
        print("%s: %s" %(threadName,time.ctime(time.time())))
        counter-=1

threadLock = threading.Lock()
threads = []

# Create Threads
thread1 = myThread(1,"Thread1",1)
thread2 = myThread(2,"Thread2",2)
thread3 = myThread(3,"Thread3",3)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()


# Add Threads To Thread List
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

#print threading.enumerate()

# Wait For All The Threads To Complete
for i in threads:
    i.join()

print("Exiting The Program")

