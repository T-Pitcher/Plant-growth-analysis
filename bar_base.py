#Status: Mostly works. 
#Work on: x axis text wrapping, multi axes on one plot, choose colours, mulit series

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('MatPlotLib\Testdata.csv', header=1)
labels = pd.read_csv('MatPlotLib\Testdata.csv')
labels=list(labels)

fig, ax = plt.subplots(constrained_layout=True)
#x = np.arange(len(data))
y1 = data['T1']
#y2 = data['T2']
#y3 = data['T3']
#y4 = data['T4']

#categories= ['T1', 'T2', 'T3']
categories = labels[1:5]
ax.bar(categories, y1[0:4], color = ['0.8', 'g', 'r', 'b']);

#ax.legend();

ax.set_xlabel('Treatment')
ax.set_ylabel('Height (cm)')
ax.set_title('Height of them (cm)', fontweight = 'bold', fontsize = 20)

# plt.ylim((0,6))
plt.ylim(bottom = 0)

plt.show()

#python matplotlib\bar_base.py