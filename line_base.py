#Status: working
# 
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('MatPlotLib\Testdata.csv', header=1)
labels = pd.read_csv('MatPlotLib\Testdata.csv')
labels=list(labels)
print(labels)

fig, ax = plt.subplots()
#x = np.arange(len(data))
y1 = data['T1']
y2 = data['T2']
y3 = data['T3']
y4 = data['T4']

ax.plot(y1, 'x', color = '0.8', linewidth = 3, label = labels[1], linestyle = '-');
ax.plot(y2, 'x', color = 'green', linewidth = 3, label = labels[2], linestyle = '-');
ax.plot(y3, 'x', color = 'k', linewidth = 3, label = labels[3], linestyle = '-');
ax.plot(y4, 'x', color = (0.3,0.3,1), linewidth = 3, label = labels[4], linestyle = '-');
#y2.set_color('green');
#y2.set_linestyle(':');


#ax.plot([1,2,3], label='Inline label')
ax.legend();
#legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

ax.set_xlabel('Weeks')
ax.set_ylabel('Height (cm)')
ax.set_title('Height of them (cm)', fontweight = 'bold', fontsize = 20)
#y1.label1()=0

#plt.plot(data, 'purple')
#plt.plot(data, 'x')


# plt.ylim((0,6))
plt.ylim(bottom = 0)
plt.xlim(left= 0)

plt.show()

#python matplotlib\line_base.py