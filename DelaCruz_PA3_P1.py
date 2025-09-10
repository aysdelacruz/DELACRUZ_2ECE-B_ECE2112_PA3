#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd  # bring in pandas so we can work with csv files and tables

# load the CSV file into a DataFrame
car_data = pd.read_csv("cars.csv")

# just showing the data (no need to use print for DataFrames)
car_data


# In[5]:


print("Here are the first and last 5 rows:")

# grabbing the top 5 and bottom 5 rows, then putting them together
sample_rows = pd.concat([car_data.iloc[:5], car_data.iloc[-5:]])

# show the result
sample_rows


# In[7]:


get_ipython().system('jupyter nbconvert --to script "DelaCruz_PA3_P1.ipynb"')

