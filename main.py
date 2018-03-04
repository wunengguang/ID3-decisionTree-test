import decsiontree
import painttree
import pandas as pd

df = pd.read_csv('E:/fazhi.csv')#读取数据
data = df.values[:,1:].tolist()#把数据除了第一列的都转换成列表
data_full=data[:]
labels=df.columns.values[1:-1].tolist()
labels_full = labels[:]
myTree=decsiontree.createTree(data,labels,data_full,labels_full)
print(myTree)
painttree.createPlot(myTree)
