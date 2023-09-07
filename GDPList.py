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


# In[26]:


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


# In[29]:


gdp_max = df['GDP (millions of US$)'].max()
gdp_min = df['GDP (millions of US$)'].min()
print("Giá trị lớn nhất của GDP:", gdp_max)
print("Giá trị nhỏ nhất của GDP:", gdp_min)


# In[30]:


mean_gdp = df['GDP (millions of US$)'].mean()
std_dev_gdp = df['GDP (millions of US$)'].std()


# In[31]:


print("Trung bình GDP:", mean_gdp)
print("Độ lệch chuẩn GDP:", std_dev_gdp)


# In[32]:


import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.hist(df['GDP (millions of US$)'], bins=30, color='blue', alpha=0.7)
plt.title('Phân phối GDP')
plt.xlabel('GDP (millions of US$)')
plt.ylabel('Số lượng quốc gia')
plt.grid(True)
plt.show()


# In[34]:


continent_counts = df['Chauluc'].value_counts()
most_common_continent = continent_counts.idxmax()
print("Châu lục xuất hiện nhiều nhất:", most_common_continent)


# In[36]:


continent_stats = df.groupby('Chauluc')['GDP (millions of US$)'].agg(['sum', 'mean']).reset_index()
continent_stats.columns = ['Tên châu lục', 'Tổng GDP', 'TBC GDP']
print(continent_stats)

