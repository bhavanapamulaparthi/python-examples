import pandas as pd
import numpy as np

x = pd.Series(data=[1,2,3,4,np.NaN], index=['a','b','c','d','e'])

y = pd.Series(['shiva','bhavana','harish'], name='Names')
df = y.to_frame()
# df = df.rename(columns= {0:'Names'})
# print(df)
# print(type(df))

a = [1,2,2,3,4,4,5,np.nan]
# print(pd.unique(pd.Series(a)))
ls = ['shiva','bhav','hari','bhav','shiva','babi']
b = pd.Series(a)
print(b.value_counts(dropna=True))


a = pd.Series(['java','c','python',np.nan])
b = a.map({'java':'core','python':'language'})
c = a.map('I know {}'.format, na_action='ignore')
# print(c)

# print(x)
# print(x.index)
# print(x.values)
# print(x.shape)
# print(x.size)
# print(x.ndim)
# print(x.dtype)
# # print(x.itemsize)
# print(x.empty)
# print(x.hasnans)
# print(x.count())
# print(len(x))