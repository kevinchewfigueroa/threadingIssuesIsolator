'''
Created on Nov 7, 2018

@author: Kevin
'''
import requests
import time
import platform 
import os
import threading

startTime = time.time()

#Returns elapsed time since thread birth
def calculateTime(start,end):
    passed = end - start
    return passed

#Returns CPU info of machine running inside Vocareum
def cpu_info():
    if platform.system() == 'Windows':
        return platform.processor()
    elif platform.system() == 'Darwin':
        command = '/usr/sbin/sysctl -n machdep.cpu.brand_string'
        return os.popen(command).read().strip()
    elif platform.system() == 'Linux':
        command = 'cat /proc/cpuinfo'
        return os.popen(command).read().strip()
    return 'platform not identified'

try:
    time.sleep(10)
    #time.sleep(178)
    endTime = time.time()
    print("\n")
    #Uncomment these two lines below, if you would like to CPU info running the threads
    #print("CPU info running this program thread:")
    #print(cpu_info())
    print("Program threadID: %d" % threading._get_ident())
    print("Program thread ran for seconds: %f" % calculateTime(startTime, endTime))
    print("Starting at: %f" % startTime)
    print("Finishing at: %f" % endTime)
    outfile = open('output.txt', 'w')
    outfile.write(str(calculateTime(startTime, endTime)))
    outfile.close()

except requests.Timeout as err:
    print ("Program-thread was interrupted, and only ran for seconds: %f" % calculateTime(startTime, time.time()))

except KeyboardInterrupt as err2:
    print ("Program-thread was interrupted, and only ran for seconds: %f" % calculateTime(startTime, time.time()))


