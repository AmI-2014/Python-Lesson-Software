'''
Created on Mar 17, 2014

@author: Dario Bonino <dario.bonino@polito.it>

Copyright (c) 2014 Dario Bonino
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
'''
import subprocess, os

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
    memory = subprocess.Popen("cat /proc/meminfo").read()
    memory_tuple = memory.split("\n")
    print "Total memory:\n \t%s"%memory_tuple[0].split(":")[1].replace(" ","")
    print "Free memory:\n \t%s"%memory_tuple[1].split(":")[1].replace(" ","")

    
    return

if __name__ == '__main__':
    print_sys_metrics()