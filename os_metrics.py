'''
Created on Mar 17, 2014

@author: bonino
'''
import os

def print_sys_metrics():    
    #get uname data
    uname = os.uname()
    
    # print the operating system information
    print "OS Type:%s\nHost:%s\nKernel:%s %s\nArch:%s\n"%uname
    
    #get the current system load average (last min, 5min, 15min)
    load = os.getloadavg()
    
    #print the load average
    print "load_avg:\n \t%f (1min)\n \t%f (5min)\n \t%f (15min)"%(load)

    # system-dependent memory info
    memory = os.popen("cat /proc/meminfo").read()
    memory_tuple = memory.split("\n")
    print "Total memory:\n \t%s"%memory_tuple[0].split(":")[1].replace(" ","")
    print "Free memory:\n \t%s"%memory_tuple[1].split(":")[1].replace(" ","")

    
    return

if __name__ == '__main__':
    print_sys_metrics()