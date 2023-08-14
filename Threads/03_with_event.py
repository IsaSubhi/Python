'''
Created on Nov 4, 2015

@author: rte
'''

import threading
from time import sleep


exitFlag = threading.Event()


threadLst = []

class myThread(threading.Thread):
    def __init__(self,threadID, name, count):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.count = count
    
    def run(self):
        print("Starting A Thread: " + self.name)
        loop_and_print(self.name, self.count, 3)
        print("Exiting A Thread: " + self.name)

def loop_and_print(name, delayTime, count):
    #while count:
    while 1:
        #if exitFlag.isSet():
        if exitFlag.wait(delayTime):
            print(name, "exiting...")
            exit()
            """
            if isinstance(name, myThread):
                name.exit()
            else:
                exit()
            """

        #sleep(delayTime)
        print("Thread Name: %s" %(name))
        count-=1

if __name__ == "__main__":
    """
    thread1 = myThread(1,"Thread1",1)
    thread2 = myThread(2,"Thread2",2)
    thread3 = myThread(3,"Thread3",3)
    
    thread1.start()
    thread2.start()
    thread3.start()
    threadLst.append(thread1)
    threadLst.append(thread2)
    threadLst.append(thread3)
    """
    
    threadLst = [
        myThread(1,"Thread1",1),
        myThread(2,"Thread2",2),
        myThread(3,"Thread3",3)
    ]
    
    for t in threadLst:
        t.start()
    
    input("press Enter to exit")
    exitFlag.set()
    print("exit flag set to 1")

    for i in threadLst:
        i.join()
    
    
    print("Exiting The Main Thread !!!...")
