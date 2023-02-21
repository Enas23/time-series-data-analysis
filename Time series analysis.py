#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()


# In[6]:


df=pd.read_csv("Downloads/multiTimeline.csv",skiprows=1)


# In[7]:


df.head()


# In[5]:


df.isnull()


# In[8]:


df.info()


# In[11]:


#wrangling my data
df.columns=['week','diet','gym','finance']
df.head()


# In[14]:


df['week']=pd.to_datetime(df['week'])


# In[15]:


df.info() #check week column from object type to datetime


# In[16]:


df.set_index('week',inplace=True)  #trying to make week column to be index  of my data 


# In[17]:


df.head()  


# In[18]:


#Exploratory data analysis(EDA)
df.plot()


# In[19]:


df[['diet']].plot()


# In[21]:


df[['diet']].rolling(12).mean() 
# using rolling funcation to achieve the smoothing concept to change seasonality to trend


# In[22]:


df[['diet']].rolling(12).mean().plot()


# In[ ]:





# In[ ]:




