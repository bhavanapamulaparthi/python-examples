import csv
import pandas as pd
from pandas import DataFrame, Series

# x = [['hari','28','mumbai'],
#       ['babi','29','hyd']]
# with open('file.csv', 'w') as file:
#     write = csv.writer(file)
#     write.writerow(['Name','Age','Location'])
#     write.writerow(['Shiva', '23', 'Knr'])
#     write.writerow(['bhavna','24','hyd'])
#     write.writerows(x)

# with open('file.csv', 'r') as file:
#     rows = csv.reader(file)
#     for row in rows:
#         print(row)

# rows = pd.read_csv('file.csv')
# print("file rows are: \n", rows)
# print("num of rows are:", rows.shape)
# print("retrieving only 2 rows:\n", rows[0:2])


C = {'Month': ['JAN','FEB', 'MAR'],
   '1958': ['345', '435', '545'],
   '1959': ['377', '135', '985'],
   '1960': ['498', '354', '765'],
}
list = [1,2,3,4,4,'shiv']
df = pd.DataFrame(C, columns= ["Month", "1958", "1959", "1960"])
file = df.to_csv('data.csv')