#Definition:
#• Matplotlib: Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It provides an
#object-oriented API for embedding plots into applications using general-purpose GUI toolkits,
#• Seabom: Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and
#informative statistical graphics.

#create a simple line plot with matplotlib
import matplotlib.pyplot as plt
#Date
x=[1,2,3,4,5]
y=[2,3,5,7,11]
#creating the line plot
plt.plot(x,y,ls="-.",color='red',lw="5",marker='*',ms=20,mfc='b')  #if nothing was added in the linestyle(ls) then the normal line will be the output. lw means linewidth. ms: marker size, mf: marker color
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple line plot')
plt.show()

import numpy as np
y1=np.array([3,8,1,10])
y2=np.array([6,2,7,11])
plt.plot(y1)
plt.plot(y2)
plt.show()

#creating a scatter plot
plt.scatter(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple scatter plot')
plt.show()

#creating a bar plot
plt.bar(x,y,color='orange',width=0.5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple bar plot')
plt.show()
#to create a horizontal bar plot, use barh instead of bar and the rest is same but the width will become height in it

#creating a histogram
data=[1,2,2,3,3,3,4,4,4,4]
plt.hist(data,bins=4)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Simple histogram')
plt.show()


#creating a subplot with matplotlib
#subplot: combination of plots

x=[1,2,3,4,5]
y1=[2,3,5,7,11]
y2=[1,4,6,8,10]
#creating subplots
fig, axs=plt.subplots(2) # this describes no.of plots in the subplot
axs[0].plot(x,y1)
axs[0].set_title('First plot')
axs[1].plot(x,y2,'tab:orange')  # it is to differentiate the two plots where the second plot contains orange color
axs[1].set_title('Second plot')
#displaying the plot
plt.tight_layout()
plt.show()

#adding annotations with matplotlib
x=[1,2,3,4,5]
y=[2,3,5,7,11]
#creating a plot with annotations
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-label')
plt.title('Plot with annotations')
plt.annotate('Peak',xy=(5,11),xytext=(4,10),arrowprops=dict(facecolor='black',shrink=0.05))
# xy describes at what value the annotation to be present
plt.show()

#creating a simple line plot with seaborn
import seaborn as sns
import matplotlib.pyplot as plt
# both seaborn and matplotlib needs to be used simultaneously
#data
x=[1,2,3,4,5]
y=[2,3,5,7,11]
#creating a line plot
sns.lineplot(x=x,y=y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple line plot with seaborn')
plt.show()

#creating a scatter plot
sns.scatterplot(x=x,y=y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple scatter plot with seaborn')
plt.show()

#creating a bar plot
sns.barplot(x=x,y=y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple bar plot with seaborn')
plt.show()

#creating a pair plot with seaborn
from sklearn.datasets import load_iris  #inbuilt dataset in sklearn package
iris=load_iris()
iris_data=sns.load_dataset("iris")  # loading the data into seaborn package to make pair plot
#creating a pair plot
sns.pairplot(iris_data,hue='species')  #hue is for colors. we are using species column in the iris dataset so different colors will be used for different kind of species
plt.title('Pair plot with seaborn')
plt.show()

#creating a heatmap with seaborn
data=np.random.rand(10,12)
sns.heatmap(data)
plt.title('Heatmap with Seaborn')
plt.show()