import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2,3],[2,5,7],[7,6,3]],columns=['col1','col2','col3'])

df.apply(lambda x:x.max() - x.min(),axis=1)

df['col1'].apply(lambda x: x*100)
df.apply(np.mean)

def adder(ele1,ele2):
   return ele1*ele2

df.pipe(adder,10)
