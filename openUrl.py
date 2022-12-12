from sys import *
import webbrowser
import re
from urllib.request import urlopen
import urllib
import validators

def is_connected():
    try:
        urllib.urlopen('http://216.58.192.142',timeout=1)
        return True
    except urllib.URLError as err:
        return False

def Find(string):
    url=re.findall('http[s]?://(?:[a-zA]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
    return url

def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            #print(line)
            #if(validators.url):
            url=Find(line)
            print(url)
            	for str in url:
                	webbrowser.open(str,new=2)


def main():

   
            WebLauncher(argv[1])

      
if __name__ =="__main__":
    main()




