#!/usr/bin/env python
# coding: utf-8

# In[129]:


import pandas as pd
import seaborn as sns
import matplotlib as plt


# In[18]:


user_data=pd.read_csv('https://stepik.org/media/attachments/lesson/360348/user_data.csv')
logs=pd.read_csv('https://stepik.org/media/attachments/lesson/360348/logs.csv')


# In[19]:


user_data.head()


# In[20]:


logs.head()


# In[22]:


logs.platform.value_counts()


# In[25]:


logs.platform.nunique()


# In[26]:


user_data.shape


# In[27]:


user_data.dtypes


# In[35]:


# count empty cells
logs.isna().sum()


# In[33]:


user_data.describe()


# In[34]:


logs.describe()


# In[45]:


success_number=logs.query('success==True')      .groupby('client', as_index=False).agg({'platform':'count'})      .rename(columns={'platform':'success_number'})      .sort_values('success_number', ascending=False)


# In[52]:


max_success=success_number.success_number.max()
success_number.query('success_number==@max_success')    .sort_values('client')    .client    .tolist()


# In[ ]:





# In[62]:


logs.query('success==True')    .groupby('platform')    .agg({'client':'count'})    .idxmax()


# In[63]:


logs.head()


# In[64]:


logs.merge(user_data, on='client')


# In[70]:


user_data_logs=logs.merge(user_data, on='client')
user_data_logs.query('premium==True').platform.value_counts()


# In[98]:


premium_data=user_data.query('premium==True')
nonpremium_data=user_data.query('premium==False')


# In[100]:


sns.displot(data=premium_data, x='age', kde=True)
sns.displot(data=nonpremium_data, x='age', kde=True)


# In[101]:


logs.head()


# In[115]:


success_count=logs.query('success==True')    .groupby('client')    .agg({'success':'sum'})
sns.displot(data=success_count, x='success', kde=False)


# In[118]:


user_data_logs.head()


# In[124]:


age_vs_successn=user_data_logs.query('platform=="computer"')    .groupby('age', as_index=False)    .agg({'success':'count'})


# In[125]:


age_vs_successn


# In[132]:


sns.barplot(x='age', y='success', data=age_vs_successn)


# In[134]:


computer_success=user_data_logs.query('platform=="computer"')


# In[136]:


sns.countplot(computer_success.age)

