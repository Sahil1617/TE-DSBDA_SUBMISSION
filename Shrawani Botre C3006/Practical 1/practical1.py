#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv("matches.csv")


# In[5]:


data.head(10)


# In[6]:


data.tail(6)


# In[7]:


data.info()


# In[9]:


data.shape


# In[17]:


data.isnull().sum()


# In[15]:


pd.isnull(data['city']).sum()


# In[18]:


data.describe()


# In[19]:


data.min()


# In[20]:


data.max()


# In[22]:


data.corr()


# In[23]:


data.value_counts()


# In[25]:


data.sort_values(by="date",ascending=True)


# In[27]:


data.groupby('Season').mean()


# In[ ]:




