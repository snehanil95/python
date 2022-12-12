#enter the name of process from user and check the process is running and display info

import psutil
from sys import *

def chkRunPro(pname):

    for p in psutil.process_iter(attrs=['pid', 'name']):
        if pname in (p.info['name']).lower():
            pinfo=p.as_dict(attrs=['pid','name','username'])
            pinfo['vms']=p.memory_info().vms/(1024*1024)
            print("yes process is running", (pinfo))

def main():

    print("Automation script started with name:",argv[0])

    if(len(argv)!=2):
        print("Error:Insufficient arguments")
        print("Use -h for help and use -u for usage of script")
        exit()

    if((argv[1]=="-h") or (argv[1]=="-H")):
        print("Help:This script is used to perform entered process is running or not")
        exit()

    if((argv[1]=="-u")or (argv[1] =="-U")):
        print("Usage:provide___number of argument as")
        print("First Argument as:program name")
        print("Secong Argument as:process name")
        exit()
    else:
        chkRunPro(argv[1])
       




if __name__ =="__main__":
    main()