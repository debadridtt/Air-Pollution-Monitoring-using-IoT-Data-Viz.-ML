
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import seaborn as sns
import datetime 
import matplotlib.dates as md


# In[71]:


df=pd.read_csv('pollution.csv')
df.head()


# In[72]:


df.drop("entry_id",axis=1,inplace=True)
df.head()


# In[73]:


#finding out the time when max. pollution occurs at Chadni Chowk
df[df['Chadni Chowk']==3.0235897439999997].drop(['Gariahat','Dharmatala'],axis=1)


# In[74]:


#finding out the time when max. pollution occurs at Gariahat
df[df['Gariahat']==3.0235897439999997].drop(['Chadni Chowk','Dharmatala'],axis=1)


# In[75]:


#finding out the time when max. pollution occurs at Dharmatala
df[df['Dharmatala']==3.0235897439999997].drop(['Chadni Chowk','Gariahat'],axis=1)


# In[96]:


#finding out pollution level at Chadni Chowk by hourly update
plt.figure(figsize=(12,8))
plt.rcParams.update({'font.size':15})
x =pd.to_datetime(df['created_at'])
y=df['Chadni Chowk']
plt.plot_date(x, y)
plt.xlabel("Data & Hour")
plt.ylabel("Pollution Level")
plt.title("Hourly Pollution Level at Chadni Chowk")


# In[97]:


#finding out pollution level at Gariahat by hourly update
plt.figure(figsize=(12,8))
plt.rcParams.update({'font.size':15})
x =pd.to_datetime(df['created_at'])
y=df['Gariahat']
plt.plot_date(x, y,color='green')
plt.xlabel("Data & Hour")
plt.ylabel("Pollution Level")
plt.title("Hourly Pollution Level at Gariahat")


# In[98]:


#finding out pollution level at Dharmatala by hourly update
plt.figure(figsize=(12,8))
plt.rcParams.update({'font.size':15})
x =pd.to_datetime(df['created_at'])
y=df['Dharmatala']
plt.plot_date(x, y,color='red')
plt.xlabel("Data & Hour")
plt.ylabel("Pollution Level")
plt.title("Hourly Pollution Level at Dharmatala")


# In[95]:


#pairplotting
sns.set(font_scale=1.5)
g=sns.pairplot(df,hue="Chadni Chowk")
g.fig.set_size_inches(15,15)


# In[108]:


sns.jointplot(x="Chadni Chowk",y="Gariahat",data=df,color='green')


# In[109]:


sns.jointplot(x="Chadni Chowk",y="Dharmatala",data=df,color='red')


# In[113]:


sns.jointplot(x="Dharmatala",y="Gariahat",data=df,color='k')

