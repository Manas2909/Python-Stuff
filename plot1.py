# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:50:51 2019

@author: Manas
"""
import matplotlib.pyplot as plt
from matplotlib import style
#import numpy as np
#plot(x,y,[fmt])
#plot y versus x as lines and/or markers.
#plt.legend()
'''
x=[1,2,3,4,5]
y=[2,3,4,2,5]
plt.plot(x,y,color="green",label='sales',linestyle="dashed",linewidth=3,marker='o',markerfacecolor="blue",markersize=12)
plt.ylim(1,8)
plt.xlim(1,8)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("some cool customization ")
plt.show()
print(plt.style.available)
style.use('classic')
'''
'''
x=[1,2,3]
y=[2,4,1]
plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("some cool customization ")
plt.show()
'''
'''
plt.plot([1,2,23,4])
plt.ylabel("some numbers")
plt.show()
'''
'''
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.axis([0,6,0,20])
plt.show()
'''
'''
t=np.arange(0.,5.,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()
'''
'''
x=[21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins=7
n,bins,patches=plt.hist(x,num_bins,facecolor="yellow",alpha=0.5)
print(n)
print(bins)
print(patches)
plt.show()
'''

x=[1,2,3,4,5]
y=[10,24,36,40,5]
tick_label=['one','two','three','four','five']
#plt.barh(x,y,tick_label=tick_label,color='red')
plt.bar(x,y,tick_label=tick_label,color='red')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("bar graph")
plt.show()

'''
web_costumer=[123,645,950,1290,1630,1450,1034,1295]
time_hrs=[7,8,9,7,6,5,6,9]
style.use('ggplot')
plt.plot(time_hrs,web_costumer,alpha=11)
plt.xlabel("hours")
plt.ylabel("no of users")
plt.title("web site traffic")
plt.axis([4,12,0,1700])
a=max(time_hrs)
b=max(web_costumer)
print(a,b)
plt.annotate("Maximum",xy=(9,1630),xytext=(8,1600),arrowprops={"facecolor":"yellow"})
plt.show()
'''
'''
x=range(10)
y=range(10)
fig,ax=plt.subplots(nrows=2,ncols=2)
print(fig)
print(ax)
for row in ax:
    print("in row loop",row)
    for col in row:
        col.plot(x,y)
plt.subplot(3,2,1)
plt.plot(x,y,"r")
plt.subplot(3,2,2)
plt.plot(x,y,"b")
'''