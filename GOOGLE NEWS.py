#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Author:Paula M -  google news searches "superspreader"

from GoogleNews import GoogleNews
googlenews = GoogleNews()


# In[1]:


from GoogleNews import GoogleNews

googlenews = GoogleNews()
googlenews.search('superspreader')
result = googlenews.result()
print(len(result))

for n in range(len(result)):
    print(n)
    for index in result[n]:
        print(index, '\n', result[n][index])


    exit()


# In[1]:


import pandas


# In[48]:


import pandas
import csv
from GoogleNews import GoogleNews
googlenews = GoogleNews()
googlenews.search('superspreader')
result = googlenews.result()
print(len(result))

for n in range(len(result)):
    print(n)
    for index in result[n]:
        print(index, '\n', result[n][index])
        
import csv
with open(r'C:\Users\messonep\FEBFC\apollo 2602\news5.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow([result])




# In[9]:


import csv


# In[ ]:




