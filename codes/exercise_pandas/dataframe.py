import tushare as ts
import pandas as pd
import numpy as np

'''
data={"one":np.random.randn(4),"two":np.linspace(1,4,4),"three":['zhangsan','李四',999,0.1]}
df=pd.DataFrame(data,index=[1,2,3,4])

print(df)

df.set_index(['one'],drop = True)

print(df)


data = np.random.randn(6,4)#6行4列
df = pd.DataFrame(data,columns=list('ABCD'),index=[1,2,'a','b','2006-10-1','第六行'])

print(df)

print(type(df.A))
print(type(df['A']))
print(type(df[['A']]))

print(type(df.loc[1]))
print(df.loc[1])

print(type(df.loc[[1,'a']]))
print(df.loc[[1,'a']])
'''

df =  ts.get_hist_data('600519')
#df =  ts.get_hist_data('600519','2020-01-01',None,'60')

print(df)

with open('.temp','w') as file_object:
    file_object.write(str(type(df)))
    file_object.write(str(df))

#print(df['close'])

print(df.columns.values)
print(df.head(2))
df = df.head(2)
#print(df['close']['2020-10-21'])

'''
简单对上面三种方法进行说明：

iterrows(): 按行遍历，将DataFrame的每一行迭代为(index, Series)对，可以通过row[name]对元素进行访问。
itertuples(): 按行遍历，将DataFrame的每一行迭代为元祖，可以通过row[name]对元素进行访问，比iterrows()效率高。
iteritems():按列遍历，将DataFrame的每一列迭代为(列名, Series)对，可以通过row[index]对元素进行访问。
'''
'''
for index,column in df.iterrows():
    print(index)#index name
'''
'''
for row in df.iterrows():
    print(row[0],row[1])
'''

for index,row in df.iteritems():
    print(index)#column name

for row in df.iteritems():
    print(row[0],row[1])

#df = ts.get_tick_data('600519','2021-02-25',src='tt')