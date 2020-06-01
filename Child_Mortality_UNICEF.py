#!/usr/bin/env python
# coding: utf-8

# In[133]:


import pandas as pd

url = 'https://raw.githubusercontent.com/dirkkoolmees/child_mortality/master/Child_Mortality_CSV.csv'
data = pd.read_csv(url,skiprows=0, index_col=0, header=1)

data.head()


# In[13]:


# importing the required libraries for plotting
import matplotlib.pyplot as plt
import matplotlib as mpl

# row counter
num_rows = 0

for row in data:
    num_rows += 1

#print(num_rows)

#Y = data[[i for i in list(data.columns) if i != 'Year']]

#this paramter allows you to set the line width, try different settings to see what it does, default is 1
mpl.rcParams['lines.linewidth'] = 1

#Rotates the x ticks if desired
plt.xticks(rotation=90)

plt.plot(data);
#plt.show()

#Notice how the years have a decimal! We'll solve this in the next plot


# In[7]:


#import numpy as np
from matplotlib.ticker import FormatStrFormatter

#changes the format of the x major ticks
fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))

#plt.xticks(rotation=45)
plt.plot(data);
#plt.show()

#Notice how the years on the x axis are a bit randomly distributed? We'll fix that in the next cell


# In[10]:


#import matplotlib.dates as mdates
#import numpy as np

#these sub-libraries allow for changing the number of ticks on the y and x axis
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
fig, ax = plt.subplots()
#This setting creates major ticks only at multiples of 40 on the y axis and multiples of 5 on the x-axis
ax.yaxis.set_major_locator(MultipleLocator(40))
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))

#This creates minor ticks (without a value) on both axis
ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))

#plt.xticks(rotation=45)
plt.plot(data);
#plt.show()


# In[42]:


#these sub-libraries allow for changing the number of ticks on the y and x axis
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
fig, ax = plt.subplots()
#Set dimensions of the figure
fig.set_size_inches(8, 5)
#This setting creates major ticks only at multiples of 40 on the y axis and multiples of 2 on the x-axis
ax.yaxis.set_major_locator(MultipleLocator(40))
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))

#This creates minor ticks (without a value) on both axis
ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))

#Note how you can change the color and transparancy - this applies to all lines
plt.plot(data, color = 'green', alpha = 0.6);

# Add a title and axis names
plt.title('Child Mortality per country - UNICEF');
plt.xlabel('Year');
plt.ylabel('Child Mortality  (death per 1000)');

ax.legend(["Haiti"], loc='best');

#plt.show()


# In[100]:


#these sub-libraries allow for changing the number of ticks on the y and x axis
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

fig, ax = plt.subplots()
#Set dimensions of the figure
fig.set_size_inches(8, 5)
#This setting creates major ticks only at multiples of 40 on the y axis and multiples of 2 on the x-axis
ax.yaxis.set_major_locator(MultipleLocator(40))
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))

#This creates minor ticks (without a value) on both axis
ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))

#color of lines
color = 'green'
color_haiti = 'red'

#selecting only the data for one particular country
data_haiti = pd.read_csv(url,skiprows=0, index_col=0, header=1, usecols = ['Year','Haiti'])

#Note how you can change the color and transparancy - this applies to all lines
plt.plot(data, color = color, alpha = 0.2);

#Plot Haiti on top so that we can manipulate the color (and possily other attributes)
plt.plot(data_haiti, color = color_haiti, alpha = 1)

# Add a title and axis names
plt.title('Child Mortality per country versus Haiti');
plt.xlabel('Year');
plt.ylabel('Child Mortality  (death per 1000)');

#Note how the legend marker has the wrong color we'll use the annotate functionality next instead
ax.legend(["Haiti"], loc='best', shadow = True, fancybox = True, bbox_to_anchor=(0.6, 0.7), frameon = True);

#plt.show()


# In[125]:


#these sub-libraries allow for changing the number of ticks on the y and x axis
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

fig, ax = plt.subplots()
#Set dimensions of the figure
fig.set_size_inches(8, 5)
#This setting creates major ticks only at multiples of 40 on the y axis and multiples of 2 on the x-axis
ax.yaxis.set_major_locator(MultipleLocator(40))
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))

#This creates minor ticks (without a value) on both axis
ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))

#color of lines
color = 'green'
color_haiti = 'red'

#selecting only the data for one particular country
data_haiti = pd.read_csv(url,skiprows=0, index_col=0, header=1, usecols = ['Year','Haiti'])

#Note how you can change the color and transparancy - this applies to all lines
plt.plot(data, color = color, alpha = 0.2);

#Plot Haiti on top so that we can manipulate the color (and possily other attributes)
plt.plot(data_haiti, color = color_haiti, alpha = 1)

# Add a title and axis names
plt.title('Child Mortality Haiti');
plt.xlabel('Year');
plt.ylabel('Child Mortality  (death per 1000)');

#annotate specific points or lines in the graph (I enter the fixed coordinates of the data point for the Earthquake here)
ax.annotate('Haiti - 2010 Earthquake',
            xy=(2010, 135), xycoords='data',
            xytext=(25, 0), textcoords='offset points',
            arrowprops=dict(facecolor= color_haiti, shrink=0.1),
            horizontalalignment='left', verticalalignment='center');

#plt.show()


# In[ ]:





# In[ ]:





# In[132]:


fig, ax = plt.subplots()
#Ready made style sheets are available, the next cell shows possible values
with plt.style.context('seaborn-deep'): plt.plot(data, alpha = 0.1);
with plt.style.context('classic'): plt.plot(data_haiti);
    
# Add title and axis names
plt.title('Child Mortality per country - UNICEF');
plt.xlabel('Year');
plt.ylabel('Child Mortality  (death per 1000)');

#annotate specific points or lines in the graph
ax.annotate('Haiti - 2010 Earthquake',
            xy=(2010, 135), xycoords='data',
            xytext=(25, 0), textcoords='offset points',
            arrowprops=dict(facecolor= color_haiti, shrink=0.1),
            horizontalalignment='left', verticalalignment='center');

#Unfortunately this returns the incorrect year notation.
#plt.show()


# In[119]:


print(plt.style.available)

