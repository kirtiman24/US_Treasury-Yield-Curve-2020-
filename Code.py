#!/usr/bin/env python
# coding: utf-8

# In[1]:



#1)a

import numpy as np
import pandas as pd
from urllib.request import urlopen  # b_soup_1.py
from bs4 import BeautifulSoup
from tabulate import tabulate

html = urlopen('https://www.treasury.gov/resource-center/'
               'data-chart-center/interest-rates/Pages/'
               'TextView.aspx?data=yieldYear&year=2020')

bsyc = BeautifulSoup(html.read(), "lxml")

fout = open('bsyc_temp.txt', 'wt',
		encoding='utf-8')

fout.write(str(bsyc))

fout.close()

# print the first table
'''print(str(bsyc.table))'''
# ... not the one we want

# so get a list of all table tags
table_list = bsyc.findAll('table')

# how many are there?
'''print('there are', len(table_list), 'table tags')

# look at the first 50 chars of each table
for t in table_list:
    print(str(t)[:50])'''

# only one class="t-chart" table, so add that
# to findAll as a dictionary attribute
tc_table_list = bsyc.findAll('table',
                      { "class" : "t-chart" } )

# how many are there?
'''print(len(tc_table_list), 't-chart tables')'''
daily_yield_curves=[]
tc_table = tc_table_list[0]
for i in tc_table.find_all('th'):
  title=i.text.strip()
  daily_yield_curves.append(title)


row_data=[]
for row in tc_table.find_all('tr')[1:]:
   data=row.find_all('td')
   row=[td.text.strip() for td in data]
   row_data.append(row)
  
daily_yield_curves.append(row_data)
print(daily_yield_curves)


# In[2]:


ls1=daily_yield_curves[0:13]


# In[3]:


print(ls1)


# In[4]:


table=tabulate(daily_yield_curves[13],headers=ls1,floatfmt=".2f")


# In[5]:


print((table))


# In[6]:


##/Users/kirtimanrai/daily_yield_curves.txt 


# In[7]:


output_path="/Users/kirtimanrai/daily_yield_curves.txt"
final_output=open(output_path,'wt',encoding='utf-8')
final_output.writelines(tabulate(daily_yield_curves[13],headers=ls1,floatfmt=".2f"))
final_output.writelines('\n')
final_output.close()


# In[52]:


#1)b
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
from matplotlib import cm


# In[96]:


g=[]
for i in range(1,252):
    g.append(i)
#print(x)

g=np.array(x)
x=g.reshape((1,251))   
x


# In[97]:


f=[1, 2, 3, 6, 12, 24, 36, 60, 84, 120, 240, 360]
f=np.asarray(f,dtype=np.float64)
y=f.reshape((12,1))
y


# In[98]:


df3=pd.DataFrame(daily_yield_curves[13][0:])
pd.to_datetime(df3[0])
e=np.asarray(df3.iloc[:,1:],dtype=np.float64)
z=e.reshape((12,251))
z


# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# from matplotlib import cm

# In[102]:


#Surface Plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection='3d')
surf = ax.plot_surface(x,y,z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_xlabel('trading days since 01/02/20')
ax.set_ylabel('Months to maturity')
ax.set_zlabel('rate')
plt.show()


# In[103]:


#Wireframe Plot

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_wireframe(x, y, z, rstride=10, cstride=10)
ax.set_xlabel('trading days since 01/02/20')
ax.set_ylabel('Months to maturity')
ax.set_zlabel('rate')

plt.show()


# In[57]:


#1)c


# In[58]:


df1=pd.DataFrame(daily_yield_curves[1:13]) #Retrieving the headers and creating a separate dataframe


# In[59]:


df1


# In[60]:


df2=pd.DataFrame(daily_yield_curves[13][0:]) #Retrieving the interest rates and dates in a separate dataframe


# In[61]:


df2.columns=ls1 #Assigning column names to this dataframe


# In[62]:


df2


# In[63]:


dfr=pd.concat([df2,df1],axis=1) 


# In[64]:


dfr


# In[65]:


dfr = dfr.iloc[: , :-1]# To remove the last column which unncessarily got created while concatenating


# In[66]:


yield_curve_df=dfr.set_index('Date')#Getting the yield curve dataframe
yield_curve_df


# In[75]:


#Converting the yield curve dataframe columns to float so that it can be plotted
yield_curve_df['1 mo'] = yield_curve_df['1 mo'].astype(float)
yield_curve_df['2 mo'] = yield_curve_df['2 mo'].astype(float)
yield_curve_df['3 mo'] = yield_curve_df['3 mo'].astype(float)
yield_curve_df['6 mo'] = yield_curve_df['6 mo'].astype(float)
yield_curve_df['1 yr'] = yield_curve_df['1 yr'].astype(float)
yield_curve_df['2 yr'] = yield_curve_df['2 yr'].astype(float)
yield_curve_df['3 yr'] = yield_curve_df['3 yr'].astype(float)
yield_curve_df['5 yr'] = yield_curve_df['5 yr'].astype(float)
yield_curve_df['7 yr'] = yield_curve_df['7 yr'].astype(float)
yield_curve_df['10 yr'] = yield_curve_df['10 yr'].astype(float)
yield_curve_df['20 yr'] = yield_curve_df['20 yr'].astype(float)
yield_curve_df['30 yr'] = yield_curve_df['30 yr'].astype(float)


# In[81]:


yield_curve_df.plot()
plt.title('Interest Rate Time Series, 2020')


# In[82]:


dft=yield_curve_df.transpose()


# In[83]:


dft


# In[84]:


by_day_yield_curve_df=dft[dft.columns[::20]]#Creating the by day yield curve dataframe


# In[85]:


#Renaming the rows by converting into integer number of months
by_day_yield_curve_df = by_day_yield_curve_df.rename({"1 mo":"1","2 mo":"2","3 mo":"3","4 mo":"4","5 mo":"5","6 mo":"6","1 yr":"12","2 yr":"24","3 yr":"36","5 yr":"60","7 yr":"84","10 yr":"120","20 yr":"240","30 yr":"360"}, axis='rows')


# In[86]:


by_day_yield_curve_df


# In[87]:


by_day_yield_curve_df.plot()
plt.title('2020 Yield Curves, 20 Day Intervals')


# In[ ]:




