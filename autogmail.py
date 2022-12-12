import smtplib
import schedule
import time
import datetime

def mail():
    server_name = "smtp.gmail.com"
    port = 465
    server = smtplib.SMTP_SSL(server_name, port)
    senders_emailid = "snehanil1112"
    receivers_emailid = "marvellousinfosystems@gmail.com"
    message_content = "Hello,i m sneha memane PPA,LB,ML testing automation mail sending script"
    password = "uqgz vcbd zmxz peuk"
    server.login("snehakalbhor22@gmail.com", password)
    server.sendmail(senders_emailid, receivers_emailid, message_content)

def main():
    schedule.every(1).minutes.do(mail)

    while(True):
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()