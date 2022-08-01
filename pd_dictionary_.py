#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


scores = {"name":['Ray','Japhy','Zosa'],
         "city":['San Francisco','San Francisco','Denver'],
         "score":[75,92,94]}


# In[3]:


df=pd.DataFrame(scores)


# In[4]:


df


# In[5]:


df['score']


# In[8]:


df['name_city']= df['name'] + '_' + df['city']


# In[9]:


df


# In[10]:


df.score


# In[11]:


df.name_city


# In[12]:


df['name_city']


# In[14]:


df[df['score']>90]


# In[ ]:




