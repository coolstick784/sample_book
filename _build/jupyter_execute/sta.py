#!/usr/bin/env python
# coding: utf-8

# In[1]:


ls


# In[2]:


import random


# In[3]:


c1 = ["b", "b"]
c2 = ["b", "b"]
c3 = ["b", "b"]
c4 = ["b", "b"]
c5 = ["b", "b"]
c6 = ["r","b"]
c7 = ["b","r"]
c8 = ["r","b"]


# In[4]:


choices = [0,1]


# In[5]:


cards = [c1, c2, c3, c4, c5, c6, c7, c8]
total = 0
blue = 0
for i in range(1000000):
    cursides = []
    
    for c in cards:
        cur_choice = random.choice(choices)
        
        if cur_choice == 0:
            other_choice = 1
        else:
            other_choice = 0
        
        if c[cur_choice] == "b":
            total += 1
            if c[other_choice] == "r":
                blue += 1
                
        
        


# In[6]:


blue/total


# In[ ]:




