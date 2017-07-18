
# coding: utf-8

# In[1]:


import sys
from qtx import qtx


# In[2]:


import pandas as pd


# In[3]:


import warnings
warnings.filterwarnings('ignore')


# In[4]:


import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
get_ipython().magic(u'pylab inline')
pylab.rcParams['figure.figsize'] = (15, 9)


# #### Select your API Endpoint

# In[5]:


api = "market-data-eod"


# #### Enter your API Token  
# You can request your trial key at https://quantextive.com/request_aex/ or via the AEX portal (https://quantextive.com/dashboard)

# In[6]:


api_key = '*****************'


# #### Enter your Endpoint parameters 

# In[7]:


params = { 
    'securityId': 'NSE:7UP',
    'startDate': '2016-11-01',
    'endDate': '2017-03-18'
}


# See a list of all companies accessible with the API at https://quantextive.com/api_company_list/   
# See a list of all available endpoints (https://quantextive.com/api_home/)

# #### Initialize the module

# In[8]:


client = qtx.ApiClient()


# #### Return data based on your parameters

# In[9]:


data = client.get(api_key, api, params).data_frame()


# #### View data sample and datatypes

# In[10]:


data.head()


# In[11]:


data.dtypes


# #### Convert integer-like columns to numeric format

# In[12]:


data2 = data.convert_objects(convert_numeric=True, copy=True)


# #### Re-index the dataframe (Set date as index)

# In[13]:


data3 = data2.set_index('date')


# In[14]:


data3.head()


# #### Visualize data

# In[15]:


data3["close_value"].plot(grid = True)


# In[ ]:




