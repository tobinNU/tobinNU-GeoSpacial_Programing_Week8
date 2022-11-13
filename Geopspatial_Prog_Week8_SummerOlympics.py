#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

    # use the following lists and dates
names = ['Athens1', 'Paris1', 'St Louis', 'London1', 'Stockolm', 'Antwerp',
         'Paris2', 'Amsterdam', 'Los Angeles1', 'Berlin', 'London2', 'Helsinki',
         'Melbourne', 'Rome', 'Tokyo', 'Mexico City', 'Munich', 'Montreal',
         'Moscow', 'Los Angeles2', 'Seoul', 'Barcelona', 'Athens', 'Sydney',
         'Athens2', 'Beijing', 'London3', 'Rio de Janiero', 'Tokyo']

dates = ['1896-04-06', '1900-05-20', '1904-07-01', '1908-04-27',
         '1912-05-05', '1920-04-20', '1924-05-04', '1928-05-17',
         '1932-07-30', '1936-08-01', '1948-07-29', '1956-11-22',
         '1960-08-25', '1964-10-10', '1968-10-12', '1972-08-26',
         '1976-07-17', '1980-07-19', '1984-07-28', '1988-09-17',
         '1992-07-25', '1996-07-19', '2000-09-15', '2004-08-13',
         '2008-08-08', '2012-07-27','2016-08-05','2021-07-21']

# Convert date strings (e.g. 1896-04-06) to datetime
dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]


# In[6]:


# Choose some nice levels
levels = np.tile([-8, 8, -4, 4, -1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
ax.set(title="Modern Summer Olympics Start dates")

ax.vlines(dates, 0, levels, color="tab:blue")  # The vertical stems.
ax.plot(dates, np.zeros_like(dates), "-o",
        color="k", markerfacecolor="w")  # Baseline and markers on it.

# annotate lines
for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")

# format xaxis with 48 month intervals
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=48))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# remove y axis and spines
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y=0.1)
plt.show()


# In[ ]:




