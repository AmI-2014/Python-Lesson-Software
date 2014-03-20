'''
Created on Mar 19, 2014

@author: bonino
'''

import os,psutil,time,tts

'''
Prints some system metric in an os-independent way
'''
def print_sys_metrics():
    #get uname data
    uname = os.uname()
    
    # print the operating system information
    print "OS Type:%s\nHost:%s\nKernel:%s %s\nArch:%s\n"%uname
    
    #get the current system load average (last min, 5min, 15min)
    load = os.getloadavg()
    
    #print the load average
    print "load_avg:\n \t%f (1min)\n \t%f (5min)\n \t%f (15min)"%(load)
    
    #get the current virtual memory statistics
    virtual_memory = psutil.virtual_memory()
    
    #print total memory
    print "Total memory:\n \t%s"%virtual_memory.total
    #print available memory
    print "Available memory:\n \t%s"%virtual_memory.available
    #print free memory
    print "Free memory:\n \t%s"%virtual_memory.available
    
    #print cpu usage
    print "CPU usage:\n \t%f"%psutil.cpu_percent(None, False)
    
    #get disk counters
    disk_io = psutil.disk_io_counters(False)
    
    #print the number of reads and corresponding bytes
    print "Reads: %d (%d bytes)"%(disk_io.read_count,disk_io.read_bytes)
    
    #print the number of writes and the corresponding bytes
    print "Writes: %d (%d bytes)"%(disk_io.write_count, disk_io.write_bytes)
    
'''
Monitors the cpu occupation and if raises over a given threshold, calls a specified function
'''
def monitor_cpu(threshold,interval,callback=None):
    while(True):
        #get the cpu percentage
        percent = psutil.cpu_percent() 
        
        #check the thrashold
        if(percent > threshold):
            
            #callback
            callback(percent)
            
            #debug
            print "calling callback: %s"%percent
        
        #wait for the given time
        time.sleep(interval)

if __name__ == '__main__':
    print_sys_metrics()
    monitor_cpu(10, 1, lambda x: tts.say("warning, CPU percent raised up to %s"%x))