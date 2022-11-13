#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib.pyplot as plt


with cbook.get_sample_data('C:\\GIS\\tobincrest.gif') as file:
    im = image.imread(file)

fig, ax = plt.subplots()

ax.plot(np.sin(25 * np.linspace(0, 1)), '-o', ms=15, alpha=0.9, mfc='blue')
ax.grid()
fig.figimage(im, 5, 5, zorder=3, alpha=.5)

plt.show()


# In[ ]:




