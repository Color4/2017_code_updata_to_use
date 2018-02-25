import numpy as np
arrary = np.array([[1,2,3],[2,3,4]])

print(arrary)

print('unmber of dim:',arrary.ndim)
print('shapw:',arrary.shape)
print('size',arrary.size)

a = np.array([10,20,30,40])
b = np.arange(4)

c = a - b
c = b**2
c = 10* np.sin(a)
c_dot = np.dot(a,b)
print(c_dot)
print(c)


A = np.arange(2,14).reshape((3,4))
print(np.argmin(A))

print(np.mean(A))
print(np.average(A))
print(A.mean())

A = np.arange(3,15)

print(A[3])

A =np.arange(3,15).reshape((3,4))
print(A[2])

print(A[1][1])
print(A[1,1:3])
print(A.flatten())

#######################################

A = np.array([1,1,1])
B = np.array([2,2,2])
print(np.vstack((A,B)))

D = np.hstack((A,B))
print(D)

print(A[np.newaxis,:])
print(A[np.newaxis,:].shape)

A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]

C = np.concatenate((A,B,B,A),axis=0)
D = np.concatenate((A,B,B,A),axis=1)
print(C)
print(D)


######################################

A = np.arange(12).reshape((3, 4))
print(np.split(A,2,axis=1)[1])
print(np.split(A, 3, axis=0))

print(np.array_split(A, 3, axis=1))

a = np.arange(4)
b = a
c = a
d = b
a[0] = 11
print(a)
print(b is a)

import pandas as pd

s = pd.Series([1,3,6,np.nan,44,1])
print(s)


dates = pd.date_range('20160101',periods= 6)
df = pd.DataFrame(np.random.randn(6,4),index = dates,columns =['a','b','c','d'])
print(df)

print(df['b'])

df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)

df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo'})
                    
print(df2)

print(df2.dtypes)
print(df2.values)

print(df2.describe())

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])

print(df['A'])
print(df.A)
print(df[0:3])

print(df['20130102':'20130104'])
print('SSSSSSSSSS')
print(df.loc['20130102'and'20130103',['A','C']])
print(df.loc['20130102',['A','C']])

print(df.iloc[3:5,1:3])
print(np.arange(1,3))
print(df.iloc[[1,3,5],[3,]])

print(df.ix[2:3,[2,3]])

df['F'] = np.nan
print(df)
df['E']=pd.Series([1,2,3,4,5,6],index = pd.date_range('20130101',periods=6))
print(df)

df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])

res = pd.concat([df1, df2, df3], axis=0)
res = pd.concat([df1,df2,df3],axis=0,ignore_index = True)

print(res)

df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])

res = pd.concat([df1, df2], axis=0, join='outer')
res = pd.concat([df1, df2], axis=0, join='inner')
print(res)


df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])

#将df2合并到df1的下面，以及重置index，并打印出结果
res = df1.append(df2, ignore_index=True)
print(res)

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)

res = pd.merge(left, right, on='key')

print(res)


import matplotlib.pyplot as plt

data = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list("ABCD")
    )
print(data)

data.cumsum()
data.plot()
#plt.show()

ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')

data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)
plt.show()

