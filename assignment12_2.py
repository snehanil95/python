#
from sys import *
import psutil
import schedule
import time
import datetime
import os



def ProcessDisplay(log_dir="Marvellous"):
    
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    seaprator="-"*80
    log_path=os.path.join(log_dir,"MarvellousLog%s.log"%(time.ctime()))
    f=open(log_path,'a')
    f.write("Process Loger:"+time.ctime()+"\n")
    f.write(seaprator+"\n")

    for pro in psutil.process_iter():
        try:
            

                pinfo=pro.as_dict(attrs=['pid','name','username'])
                pinfo['vms']=pro.memory_info().vms/(1024*1024)
                listprocess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

        
    for element in listprocess:
        f.write("%s\n"%element)
    
    return listprocess

def main():
    print("process monitor")

    
    

    

    listprocess=ProcessDisplay(argv[1])
    print(listprocess)
    

    

if __name__ =="__main__":
    main()
