'''
Created on Nov 4, 2015

@author: rte
'''


import queue,threading,time

exitFlag = threading.Event()


class myThread(threading.Thread):
    def __init__(self,threadID,name,myQueue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.myQueue = myQueue
    
    def run(self):
        print("Starting: " + threading.currentThread().getName())
#         print "Starting: " + threading.Thread.getName(self)
        myFunction(self.name,self.myQueue)
        print("Exiting: " + self.name)

def myFunction(threadName, myQueue):
    #while not exitFlag:
    while not exitFlag.is_set():

        """
        if not currQueue.empty():
            
            qItem = myQueue.get()
            print("%s processing %s\n" %(threadName,qItem))
        """

        try:
            qItem = myQueue.get(block=False)
            print("%s processing %s\n" %(threadName,qItem))
        except queue.Empty:
            pass
            
        #queueLock.release()
        time.sleep(1)
        

threadLst = ["Thread1","Thread2","Thread3","Thread4"]
lst = ["1st","2nd","3rd","4th","5th","6th","7th","8th"]
#queueLock = threading.Lock()
currQueue = queue.Queue(10) # 10 is the Max Size Of The Queue
threads = []
threadID = 1

# Create New Threads
for i in threadLst:
    thread = myThread(threadID, i, currQueue)
    thread.start()
    threads.append(thread)
    threadID+=1

# Add Threads To currQueue
for w in lst:
    currQueue.put(w)

# Wait Until currQueue Is Empty
while not currQueue.empty():
    pass

# print threads[1].isAlive()
# Modify The Flag For Thread To Exit myFunction

exitFlag.set()

# Wait For All The Threads To Complete
for i in threads:
    i.join()

# print threads[1].isAlive()

print("Exiting The Program")




