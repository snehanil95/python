import psutil
import schedule
import time
import datetime



def ProcessDisplay():
    
    listprocess=[]

    for pro in psutil.process_iter():
        try:
            pinfo=pro.as_dict(attrs=['pid','name','username'])
            pinfo['vms']=pro.memory_info().vms/(1024*1024)
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    
    return listprocess

def main():
    print("process monitor")

    
    

    fd1=open("Marvellous%s.log"(ctime.time()),"w")

    listprocess=ProcessDisplay()
    

    for no in listprocess:
        
        fd1.write(str(no))


    fd1=open("Marvellous","r")
    print("file content:",fd1)
    print(fd1.read())
        


if __name__ =="__main__":
    main()
