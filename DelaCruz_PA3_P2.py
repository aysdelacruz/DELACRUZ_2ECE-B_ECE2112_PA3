#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

cars = pd.read_csv('cars.csv')
cars


# In[4]:


# selecting only the odd-numbered columns (like column 0, 2, 4, etc.)
odd_columns = cars.iloc[:, ::2]

# get the first 5 rows from the selected columns
top_odd_columns = odd_columns.head()

# display them
odd_columns
top_odd_columns


# In[ ]:




