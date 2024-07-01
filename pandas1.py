#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


ages={'s':5,'p':6,'a':4}
pd.Series(ages)


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


q1={'japan':80,'china':450,'india':200,'usa':250}
q2={'brazil':100,'china':500,'india':210,'usa':260}


# In[4]:


sales_q1=pd.Series(q1)
sales_q2=pd.Series(q2)


# In[5]:


sales_q1['japan']


# In[6]:


sales_q2['india']


# In[7]:


sales_q1.keys()


# In[8]:


sales_q1.values


# In[9]:


sales_q1*3


# In[10]:


sales_q1+sales_q2


# In[14]:


sales_q1.add(sales_q2,fill_value=0)


# ## DataFrame

# In[19]:


np.random.seed(101)
mydata=np.random.randint(0,101,(4,3))
mydata


# In[20]:


mydata


# In[21]:


myindex=['ca','nz','ja','br']
mycolumn=['p','m','o']


# In[27]:


df=pd.DataFrame(mydata)
df


# In[31]:


df=pd.DataFrame(data=mydata,index=myindex,columns=mycolumn)
df


# In[32]:


df.info()


# In[33]:


pwd


# In[36]:


ls


# In[40]:


df=pd.read_csv('C:\\Users\\pujad\\python crash course\\tips.csv')


# In[41]:


df


# In[42]:


df=pd.read_csv('diabetes.csv')
df


# In[ ]:




