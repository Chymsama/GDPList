#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import re


# In[3]:


data_path = 'D:\\codegym3\\'
data_name = 'GDPlist.csv'

df = pd.read_csv(data_path+data_name, encoding= 'unicode_escape')

df.head(3)


# In[6]:


df = df.rename(columns={'Country': 'Nuoc', 'Continent': 'Chauluc', 'GDP (triệu USD)': 'GDP (trieu $'})
df.head(3)


# In[14]:


df.insert(df.columns.get_loc('Nuoc')+1,'Thanhphone',df['Nuoc'])
df.head()



# In[16]:


df.head(3)


# In[17]:


df['Thanhpho']=df['Thanhpho'].replace({'Việt Nam': 'Hanoi', 'Mỹ': 'Washington', 'Trung Quốc': 'Bắc Kinh'})


# In[20]:


df.head(9)


# In[22]:


df= df.drop(df[df['Chauluc']=='Asia'].index)


# In[23]:


df.head(9)


# In[24]:


df= df.drop(df[df['GDP (millions of US$)']<300000].index)


# In[25]:


df.head(9)

