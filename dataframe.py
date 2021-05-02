import pandas as pd

dict = {'Emps':['shiva','hari','babi'],'Dept':['IT','CSE','EEE']}

info = {'one':pd.Series([1,2,3,4],index=['a','b','c','d']),
        'two':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])}

df = pd.DataFrame(info)
# print(df.loc['c'])
# print(df.iloc[3])
# print(df[2:4])
# adding columns
df['three'] = pd.Series([10,20,30],index=['a','b','c'])
df['four'] = df['one'] + df['three']
# print(df)

# deleting cols
del df['two']
df.pop('four')

# print(df)
import pandas as pd
import numpy as np

a_info = pd.DataFrame({'x':[1,2,3,4],'y':[6,7,8,9]})
b_info = pd.DataFrame({'x':[1,2,3],'y':[6,7,8],'z':[3,4,5]})

c_info = a_info.append(b_info, ignore_index=True)
# print(c_info)

info = pd.DataFrame([[2, 7]] * 4, columns=['P', 'Q'])
# print(info.apply(np.sqrt))
# print(info.apply(np.sum, axis=1))
# print(info.apply(lambda x: [1, 2], axis=1, result_type='broadcast'))
# print(info.apply(lambda x: pd.Series([1, 2], index=['foo', 'bar']), axis=1))
inf =pd.DataFrame([[1,5,7],[10,12,15],[18,21,24],[np.nan,np.nan,np.nan]],columns=['X','Y','Z'])
print(inf)
print(inf.agg('sum'))
print(inf.agg(['min','max']))
print(inf.agg({'X':['sum','min','max'], 'Y':['sum','min','max']}))