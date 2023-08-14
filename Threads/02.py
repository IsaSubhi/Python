'''
Created on Nov 4, 2015

@author: eimad
'''


import _thread
from time import sleep


def threadFunction(name,sleepTime):
    count = 0
    while count < 5:
    #while count < 10000000:
        sleep(sleepTime)
        count+=1
        print("Thread Name: ----> \"{0}\"\n".format(name))
    

if __name__ == "__main__":
    try:
        _thread.start_new_thread(threadFunction, ("firstThread",5))
        #_thread.start_new_thread(threadFunction, ("secondThread",3))
        _thread.start_new_thread(threadFunction, (), {'sleepTime': 3, 'name': "secondThread"})

        #sleep(3)
        print(_thread._count())
    except:
        print("Error: Unable To Start A New Thread")
    
    while 1:
        pass
        
    
