'''
Created on Mar 23, 2016

@author: eimad
'''


import os, re

received_packages = re.compile(r"(\d) received")
status = ("no response","alive but losses","alive")

for suffix in range(20,30):
    ip = "192.168.0."+str(suffix)
    ping_out = os.popen("ping -q -c2 "+ip,"r")
    print("... pinging ",ip)
    while True:
        line = ping_out.readline()
        if not line: break
        n_received = received_packages.findall(line)
        #n_received = re.findall(r"(\d) received", line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])
