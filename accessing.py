#!/usr/bin/env python
# coding: utf-8

# In[1]:


import main as x # importing the main file, here 'main' is the name of the file i used  


# In[2]:


x.create("UG",10) #creating key and value with no time to live property
x.create("PG",20,120) #creating key and value with time to live property


# In[3]:


x.read("UG") #it returns the value of the respective key in Jasonobject format 'key_name:value'


# In[4]:


x.read("PG") #it returns the value of the respective key in Jasonobject format 'key_name:value'


# In[5]:


x.read("PG") #it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


# In[7]:


x.modify("UG",30) #modifying the value for key
x.read("UG")      #it returns the value of the respective key in Jasonobject format 'key_name:value'


# In[8]:


x.delete("UG") #it deletes the respective key and its value from the database


# In[9]:


x.read("UG") #returns key not exist in database


# In[10]:


x.create("@123",50) #returns key_name must contain only alphabets and no special characters or numbers


# In[11 ]:
#using multiple threads 
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()






