import schedule
from sys import *
import os
import hashlib
import time
import email, smtplib, ssl
import functools

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from collections import defaultdict


default_factory = (lambda: list(range(0,5)))
d = defaultdict(default_factory)


def mailsent(rmail):
    subject = "Duplicates files are:"
    body = "Do you want to delete it:"
    sender_email = "snehakalbhor22@gmail.com"
    receiver_email =rmail
    password = input("Type your password and press enter:")
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = ("DupsFile%s.log"%(time.ctime())) # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    print("Mail sent sucessfully")


def Deletefiles(dict1):
    print(dict1)
    results=list(filter(lambda x:len(x)>1,dict1.values()))

    iCnt=0

    if(len(results)>0):
        for result in results:
            for subresult in result:
                iCnt+=1
                if iCnt>=2:
                    os.remove(subresult)
        iCnt=0
    else:
        print("No duplicate found")
        

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf=afile.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def findDup(path):
    flag=os.path.isabs(path)

    if flag==false:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    dups={}

    if exists:
        for dirName,sundirs,fileList in os.walk(path):
            print("Current folder :"+dirName)
            for filen in fileList:
                path=os.path.join(dirName,filen)
                file_hash=hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]

        return dups

    else:
        print("Invalid path")


def printResult(dict1):
    separator="-"*80

    fd=open("DupsFile%s.log"%(time.ctime()),'a')
    fd.write(separator+"\n")
    fd.write("Duplicates files:")
    fd.write("\n"+separator+"\n")
    results=list(filter(lambda x:len(x)>1,dict1.values()))

    if len(results)>0:
        #print("Duplicates found")
        #f.write("the following are duplicates:")

        for result in results:
            for subresult in result:
                fd.writelines('\t\t%s'%subresult)

    else:
        fd.write("No duplicates found")

def DisplayChecksum(Dir_Name):
    #flag=os.path.isabs(path)
    #print(flag)
    
    dups={}
    print("*")
    for foldername, subfolder, Filenames in os.walk(Dir_Name):
        print("**")
        print("Folder name is : "+foldername)
        for subf in subfolder:
            print("Subfolder name of "+foldername+" is "+subf)
        for fnames in Filenames:
            print("File inside folder "+foldername+" is "+fnames)
            path=os.path.join(foldername,fnames)
            file_hash=hashfile(path)

            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash]=[path]
    #print(dups)
    return dups


def main():

    print("Automation script started with name:",argv[0])

    if(len(argv)!=3):
        print("Error:Insufficient arguments")
        print("Use -h for help and use -u for usage of script")
        exit()

    if((argv[1]=="-h") or (argv[1]=="-H")):
        print("Help:This script is used to perform duplicates file in current directory")
        exit()

    if((argv[1]=="-u")or (argv[1] =="-U")):
        print("Usage:provide___number of argument as")
        print("First Argument as:Directory name")
        print("Second Argument as:scheduler time")
        print("Third Argument as:Receiver mail id")
        exit()
    else:
        #fd=open("DupFile","a")
        arr=DisplayChecksum(argv[1]) 
        #fd.writelines(arr)
        printResult(arr)
        #mailsent(argv[2])
        #Deletefiles(arr)
        #print(arr) 
        Rmailid=argv[2]
        schedule.every(2).minutes.do(mailsent(Rmailid))

        while(True):
            schedule.run_pending()
            time.sleep(1)          
        

if __name__ =="__main__":
    main()
