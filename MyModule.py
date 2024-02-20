#!/usr/bin/env python
# coding: utf-8

# In[1]:


def checkifnotnum(*args):
    for x in args:
        if not(isinstance(x,(int,float))):
            return False
    return True

def universaladdallnums(*args):
    s=0
    for x in args:
        s+=x
    return s


myname='Python'
    
    
    


# In[ ]:




