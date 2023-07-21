#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pypolt as ply


# In[ ]:





# In[ ]:





# In[20]:


import os


# In[ ]:





# In[ ]:





# In[26]:


os.listdir(r"C:\Users\harsh\Downloads\Datasets-20230718T152140Z-001\Datasets")


# In[8]:


uber_15 = pd.read_csv(r"C:\Users\harsh\Downloads\Datasets-20230718T152140Z-001\Datasets\uber-raw-data-janjune-15_sample.csv")


# In[9]:


uber_15.shape


# In[10]:


type(uber_15)


# In[ ]:





# In[6]:


uber_15.duplicated()


# In[ ]:





# In[11]:


uber_15.duplicated().sum()


# In[ ]:





# In[35]:


uber_15.drop_duplicates(inplace= True)


# In[36]:


uber_15.duplicated().sum()


# In[12]:


uber_15.shape


# In[ ]:





# In[39]:


uber_15.dtypes


# In[41]:


uber_15.isnull().sum()


# In[46]:


type(uber_15 ['Pickup_date'][0])


# In[51]:


uber_15['pickup_date']= pd.to_datetime(uber_15['Pickup_date'])


# In[53]:


uber_15['pickup_date'] .dtype


# In[54]:


uber_15['pickup_date'][0]


# In[56]:


type(uber_15['pickup_date'][0])


# In[57]:


uber_15.dtypes


# In[13]:


uber_15


# In[ ]:





# In[66]:


uber_15['pickup_date'].dt.month_name()


# In[67]:


uber_15['month'] = uber_15['pickup_date'].dt.month_name()


# In[72]:


uber_15['month'].value_counts().plot(kind='bar')


# In[7]:


uber_15['weekday']= uber_15['pickup_date'].dt.day_name()


# In[ ]:





# In[ ]:





# In[77]:


uber_15['day']= uber_15['pickup_date'].dt.day


# In[78]:


uber_15['hour']= uber_15['pickup_date'].dt.hour


# In[ ]:





# In[79]:


uber_15['minute']= uber_15['pickup_date'].dt.minute


# In[82]:


uber_15.head(4)


# In[89]:


pivot = pd.crosstab(index=uber_15['month'], columns = uber_15['weekday'])


# In[90]:


pivot 


# In[93]:


pivot.plot(kind = 'bar',figsize = (8,6))


# lets Find our hourly rush in new york city on all days

# In[2]:


uber_15


# In[3]:


pivot


# In[ ]:





# In[97]:


pivot


# In[103]:


uber_15["weekday"]


# In[106]:


summary =uber_15.groupby(['weekday','hour'], as_index = False).size()


# In[107]:


summary


# In[108]:


sns.pointplot(x= "hour",y="size",hue = "weekday",data= summary)


# which Base_number has most number fo active vechicles ??

# In[16]:


uber_15


# In[18]:


uber_15.columns


# In[21]:


os.listdir(r"C:\Users\harsh\Downloads\Datasets-20230718T152140Z-001\Datasets")


# In[23]:


uber_foil =pd.read_csv(r"C:\Users\harsh\Downloads\Datasets-20230718T152140Z-001\Datasets/Uber-Jan-Feb-FOIL.csv")


# In[25]:


uber_foil.shape


# In[27]:


uber_foil.head(3)


# In[28]:


get_ipython().system('pip install  chart_studio')
get_ipython().system('pip install plotly')


# In[32]:


import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px


from plotly.offline import download_plotlyjs,init_notebook_mode,plot, iplot 


# In[33]:


init_notebook_mode(connected = True)


# In[34]:


uber_foil.columns


# In[35]:


px.box(x='dispatching_base_number',y= 'active_vehicles',data_frame= uber_foil)


# In[36]:


px.violin(x='dispatching_base_number',y= 'active_vehicles',data_frame= uber_foil)


# Collect entire data and use it !

# In[39]:


files = os.listdir(r"C:\Users\harsh\Downloads\Datasets-20230718T152140Z-001\Datasets")[-8:-1]


# In[40]:


files


# In[41]:


files.remove('uber-raw-data-janjune-15.csv')


# In[42]:


files


# In[43]:


files.remove('uber-raw-data-janjune-15_sample.csv')


# In[44]:


files


# In[52]:


final = pd.DataFrame()

path = r"C:\Users\harsh\Downloads\Datasets-20230718T152140Z-001\Datasets"
for file in files :
    current_df = pd.read_csv(path + '/' + file)
    final = pd.concat([current_df,final])


# In[54]:


final.shape


# In[57]:


final.duplicated().sum()


# In[59]:


final.drop_duplicates(inplace= True)


# In[61]:


final.shape


# In[62]:


final.head(3)


# At what locations of new york city we are getting rush ??

# In[64]:


rush_uber = final.groupby(['Lat','Lon'], as_index= False).size()


# In[65]:


rush_uber.head(6)


# In[66]:


get_ipython().system('pip install folium')


# In[69]:


import folium


# In[70]:


basemap = folium.Map()


# In[71]:


basemap


# In[72]:


from folium.plugins import HeatMap


# In[74]:


HeatMap(rush_uber).add_to(basemap)


# In[75]:


basemap


# Examine rush on Hour and weekday(Perform Pair wise Analysis)

# In[78]:


final.columns


# In[79]:


final.head(3)


# In[80]:


final.dtypes


# In[81]:


pd.to_datetime(final['Date/Time'])


# In[83]:


final['Date/Time'][0]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


uber_15['pickup_date'].dt.day_month()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




