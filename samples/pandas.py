
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np


# In[13]:


# Leer de diferentes funtes

# data = pd.read_sql_query("SELECT * FROM TABLE")

data = pd.read_csv("/Users/angul/Documents/R/PyCourse/data/data.csv")
data = pd.read_excel("/Users/angul/Documents/R/PyCourse/data/data.xls")


# In[14]:


data.head()


# In[16]:


data.corr()


# In[ ]:


np

