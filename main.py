#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import threading 
from threading import*
import time

d={} # dictionary in which we store data

#for create operation ->syntax "create(key_name,value,timeout_value)" 
def create(key,value,timeout=0):
    if key in d:
        print("Error: This key already exists") #error message
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
            else:
                print("Error: Memory limit exceeded!! ")#error message
        else:
            print("Error: Invalid key_name!! key_name must contain only alphabets and no special characters or numbers")#error message

#for read operation ->use syntax "read(key_name)"
            
def read(key):
    if key not in d:
        print("Error: Given key does not exist in database. Please enter a valid key") #error message
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("Error: time-to-live of",key,"has expired") #error message
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in d:
        print("Error: given key does not exist in database. Please enter a valid key") #error message
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("Key is successfully deleted")
            else:
                print("Error: time-to-live of",key,"has expired") #error message
        else:
            del d[key]
            print("Key is successfully deleted")

#for modify operation -> use syntax "modify(key_name,new_value)"

def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("Error: given key does not exist in database. Please enter a valid key") #error message
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("Error: time-to-live of",key,"has expired") #error message
    else:
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key") #error message
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l

