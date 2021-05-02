import pandas as pd
import numpy as np

info = pd.DataFrame({'t_c':[10,40]},index=['india','Germany'])

info.assign(**{'t_f' :lambda x:x.t_c * 2, 't_k':lambda x:x['t_c'] * 5})

x = pd.DataFrame({'A':[1,2,3,4],'B':['a','b','c','d'],'categorical':pd.Categorical(['s','t','u','d'])})
x.dtypes
x.astype({'A': 'int32'}).dtypes
x.dtypes
x.count(axis=1)
y = pd.Series([1,2,3])
x.describe(include=['category'])

data = {'Name': ['Parker', 'Smith', 'John', 'William'],
        'Percentage': [82, 98, 91, 87],
        'Course': ['B.Sc', 'B.Ed', 'M.Phill', 'BA']}
df = pd.DataFrame(data)
df.head()

grouped = df.groupby('Course')
print(df.groupby('Course').filter(lambda x: len(x) >= 1))

import matplotlib
d = pd.DataFrame({'length':[2,1.9,3.2,4],'breadth':[1.8,2.0,3.2,5.2]})
hist = d.hist(bins=4)
d.mean(axis=1)
data = pd.read_csv("data.csv")
a = pd.DataFrame([[1,2],[3,4]],index=['P','Q'])
for ind,row in a.iterrows():
        print(ind, row)

left = pd.DataFrame({'key': ['K0', 'K1', 'K2','K3'],
                      'A': ['A0', 'A1', 'A2','A3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                       'B': ['B0', 'B1', 'B2']})
left.join(right, lsuffix='_A', rsuffix='_B')
left.set_index('key').join(right.set_index('key'))
left.join(right.set_index('key'),on='key')

pd.merge(left,right,on='key')

info = pd.DataFrame({'P': ['Smith', 'John', 'William', 'Parker'],
      'Q': ['Python', 'C', 'C++', 'Java'],
      'R': [19, 24, 22, 25],
      'S':[20,12,15,24]})

pd.pivot_table(info,index=['P','Q'])




info = pd.DataFrame({'X': range(1, 6),
                    'Y': range(10, 0, -2)})
info.query('X>Y')
info[info.X > info.Y]
info.rename(columns={'Y':'Z'})
info.columns



info = pd.DataFrame({'data1': [2, 4, 8, 0],
                        'data2': [2, 0, 0, 0],
                        'data3': [10, 2, 1, 8]},
                        index=['John', 'Parker', 'Smith', 'William'])
info
info['data1'].sample(n=3)
info.sample(frac=0.5, replace=True, random_state=1)
info.sample(n=2,weights='data3')
info.shift(periods=2,fill_value=40)
info.sort_values(by='data2')


df = pd.DataFrame(np.random.randn(10,2),index=[3,2,5,7,8,9,6,4,1,0],columns=['col1','col2'])
df.sort_index(axis=1)