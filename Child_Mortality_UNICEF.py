#!/usr/bin/env python
# coding: utf-8

# In[69]:


import pandas as pd

import matplotlib.pyplot as plt

import matplotlib as mpl
from cycler import cycler
#plt.style.use('ggplot')
url = 'https://raw.githubusercontent.com/dirkkoolmees/child_mortality/master/Child_Mortality_CSV.csv'
data = pd.read_csv(url,skiprows = 0, index_col=0,header = 1, dtype = {"Year":"int64"})

#data = data.set_index("Year")

data.head()


# In[110]:




num_rows = 0

for row in data:
    num_rows += 1

#print(num_rows)

#Y = data[[i for i in list(data.columns) if i != 'Year']]
#mpl.rcParams['lines.linewidth'] = 0.4
plt.xticks(rotation=45)

plt.plot(data);
#plt.show()


# In[111]:


import matplotlib.dates as mdates
import numpy as np
from matplotlib.ticker import FormatStrFormatter

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))

#years = mdates.YearLocator()   # every year
#years_fmt = mdates.DateFormatter('int64')

# format the ticks
#ax.xaxis.set_major_locator(years)
#ax.xaxis.set_major_formatter(years_fmt)

#fig, ax = plt.subplots()
#ax.plot('date', 'adj_close', data=data)

#plt.grid(False)

#ax.xaxis_date()
#plt.format_xdata = mdates.DateFormatter('integer')
#fig.autofmt_xdate()
plt.xticks(rotation=45)
plt.plot(X, Y);
#plt.show()


# In[ ]:





# In[4]:


with plt.style.context('Solarize_Light2'): plt.plot(X, Y);

plt.show()


# In[8]:


print(plt.style.available)

