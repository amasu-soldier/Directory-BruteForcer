#!/usr/bin/env python

import requests
import os
from urllib import *

'''This brute_forcer method get url  from the user and perform bruteforcing on directories'''

def brute_forcer():
    userInputedUrl=input("Enter URL:")
    directory_list=open("directory.txt",'r') 

    OK="200 OK"
    Not_OK="404 Error"
    found_dir=[]

    for item in (directory_list):
        requestParameters=userInputedUrl+"/"+item
        requestParameters=requestParameters.rstrip('\n')
        response=requests.get(requestParameters)
        
        if response.status_code == 200:
            print("%s Found %s" %(OK,item))
            found_dir.append(item)
	
        else:
            print("%s Not Found %s" % (Not_OK,item))
    print("(***Found Directories***)")
    Printer(found_dir)
    

'''This Printer method print those directories which are found during bruteforcing one by one'''

def Printer(found_dir):
    for item in found_dir:
        print(item.rstrip(''),end='')



'''Starting Point of the program'''

if __name__=="__main__":
    brute_forcer()

