'''
Created on Nov 9, 2015

@author: rte
'''

import threading
import time


def firstFunction(*args):
	print(threading.currentThread().getName(), 'Starting')
	time.sleep(2)
	for i in args:
		print("keywords: %s" %(i))
	print(threading.currentThread().getName(), 'Exiting')


def secondFunction(*args):
	print(threading.currentThread().getName(), 'Starting')
	time.sleep(2)
	for i in args:
		print("keywords: %s" %(i))
	print(threading.currentThread().getName(), 'Exiting')

th1 = threading.Thread(name='Thread1', target=firstFunction,args=(3,5,7))
th2 = threading.Thread(name='Thread2', target=secondFunction)
th3 = threading.Thread(name='Thread3', target=firstFunction,args=(1,2,4))

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()

print("End Of Program")
