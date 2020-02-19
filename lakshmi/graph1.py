import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
good=[]
bad=[]

value=[]
index = np.arange(10)
df=pd.read_csv("trustvalue.csv")
for i in range(1,6,2):
	good.append(df.iloc[i-1,0])
	value.append(df.iloc[i-1,1])
print(good)
print(value)
var="LAPTOP"
df.plot('PROVIDER',var,kind='bar',align='edge',width=0.5)
plt.show()
