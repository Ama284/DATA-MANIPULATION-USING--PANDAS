#!/usr/bin/env python
# coding: utf-8

# # Series object in pandas

# In[2]:


import pandas as pd
data=[1,2,3,4,5,6]
series1=pd.Series(data)
series1


# In[3]:


type(series1)  # check the type  


# In[7]:


# Change the index of the series object

series1=pd.Series(data, index = ['a', 'b', 'c', 'd', 'e', 'g'])
series1


# In[7]:


import pandas as pd   # random number print
import numpy as np
s=pd.Series(np.random.randn(4))
s


# In[8]:


ts=pd.Series(10, index=['a','b', 'c','d'])    # constant number passed as data for series representation
ts


# In[9]:


ts1=pd.Series(range(3), index=['A','B','C'])   # using range
ts1


# In[11]:


ts2=pd.Series(np.arange(1,20,7), index=['A','B','C'])
ts2


# In[13]:


ts3=pd.Series(np.array(np.arange(1,20,7)),index=['A','B','C'])  # using one dimensional array
ts3


# In[15]:


ts4=pd.Series(np.array([np.arange(1,20,7)]),index=['A','B','C'])  # using two dimensional array
ts4


# # How to create Data Frame

# In[9]:


# creating a data frame using a list
import pandas as pd
data =[1,2,3,4,5]
df=pd.DataFrame(data)
df


# In[10]:


# creating a data frame using a dictionary

dictionary={'fruits': ['apple', 'banana', 'mangoes'], 'count': [20,30,40]}
df= pd.DataFrame(dictionary)
df


# In[11]:


# creating a data frame using a series

series=pd.Series([6,12], index=['a', 'b'])
df = pd.DataFrame(series)
df


# In[18]:


# creating a data frame using a numpy array

import numpy as np
numpyarray = np.array([[50000,60000,70000],['Amit', 'Gautam', 'Deep']])
df = pd.DataFrame({'name' :numpyarray[1], 'salary' :numpyarray[0]})
df


# # How to perform merge opertaion 

# In[25]:


import pandas as pd
player=['Player1', 'Player2','Player3']
points=[6,8,9]
title=['Game1','Game2','Game3']
df1 = pd.DataFrame({'Player':player, 'Points':points,'Title':title})
df1


# In[24]:


player=['Player1', 'Player5', 'Player6']
power=['Punch', 'Kick', 'Elbow']
title=['Game1', 'Game5','Game6']
df2=pd.DataFrame({'Player':player, 'Power':power, 'Title':title})
df2


# In[32]:


#INNER MERGE

df1.merge(df2, on='Player', how='inner')


# In[31]:


# LEFT MERGE
df1.merge(df2, on='Player', how='left')


# In[30]:


# RIGHT MERGE
df1.merge(df2, on='Player', how='right')


# In[33]:


# OUTER MERGE
df1.merge(df2, on='Player', how='outer') 


# In[48]:


# How to perform JOIN Operation in Pandas:

player=['Player1', 'Player5', 'Player6']
power=['Punch', 'Kick', 'Elbow']
title=['Game1', 'Game5','Game6']
df3=pd.DataFrame({'Player':player, 'Power':power, 'Title':title}, index=['L1','L2','L3'])
df3


# In[51]:


player=['Player1', 'Player5', 'Player6']
power=['Punch', 'Kick', 'Elbow']
title=['Game1', 'Game5','Game6']
df4=pd.DataFrame({'Players':player, 'Powers':power, 'Titles':title}, index=['L2','L3','L4'])
df4


# In[52]:


#INNER JOIN
# in join case two dataframe is join on the basis of index name but in merge the two data frame is merge on the basis of attributes name 

df3.join(df4, how = 'inner')


# In[54]:


#LEFT JOIN
df3.join(df4, how = 'left')


# In[55]:


#RIGHT JOIN
df3.join(df4, how = 'right')


# In[56]:


#OUTER JOIN
df3.join(df4, how = 'outer')

