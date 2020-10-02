#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import pandas library
import pandas as pd
import numpy as np


# In[2]:


csv_path = 'https://s3.us.cloud-object-storage.appdomain.cloud/cf-courses-data/CognitiveClass/DP0701EN/version-2/Data-Collisions.csv'
df = pd.read_csv(csv_path)
df_bk = df.copy()


# In[8]:


df.head(1)


# In[5]:


df['SEVERITYCODE'].value_counts().to_frame()


# In[6]:


df.shape


# In[9]:


df['ROADCOND'].isnull().sum()


# In[ ]:




