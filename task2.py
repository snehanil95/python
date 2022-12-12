import schedule
import time
import datetime
import sys
def Task_Minute():
    print("Task based on minutes gets scheduled at:",datetime.datetime.now())

def Task_Hour():
    print("Task based on hour gets scheduled at:",datetime.datetime.now())

def Task_Day():
    print("Task based on day gets scheduled at:",datetime.datetime.now())

def Task_Terminator():
    sys.exit()

def main():
    print("Inside task scheduler:")
    print("Current time is:",datetime.datetime.now())
    schedule.every(1).minutes.do(Task_Minute)
    schedule.every(1).hour.do(Task_Hour)
    schedule.every().saturday.at("21:17").do(Task_Day)
    schedule.every(5).minutes.do(Task_Terminator)

    
    while(True):
        schedule.run_pending()
        time.sleep(1)

        



if __name__ =="__main__":
    main()