import pandas as pd
import os
import mysql.connector

dir = r'/Users/harish/project/python-examples/tag_files/'
images_df = pd.DataFrame(columns=['File_Name', 'Images', 'Back_or_front', 'File_loc'])
f_df = pd.DataFrame(columns=['File_Name', 'Time_Stamp', 'Tag_ID', 'Facility_Code', 'Plaza_Code', 'Lane_Code', 'Vehicle_Speed'])

for filename in os.listdir(dir):
    if filename.endswith(".tag"):

        full_path = os.path.join(dir, filename)

        df = pd.read_csv(full_path,sep='=')

        df1 = df.dropna()
        # print(df1.index)
        df1.insert(0,"Columns",df1.index)
        df1.columns = ['Columns','Values']
        data = df1.reset_index(drop=True)

        data['Columns'] = data['Columns'].apply(lambda x:x.strip())
        data['Values'] = data['Values'].apply(lambda x:x.strip())
        images_list=['BACK_SHOT_1','BACK_SHOT_2','FRONT_SHOT_1']
        images = data[data['Columns'].isin(images_list)]
        images.columns = ['Back_or_front','Images']
        images = images[['Images','Back_or_front']]
        images.insert(0,'File_Name',filename)
        images.insert(3,'File_loc',full_path)

        features_list = ['File_Name','Time_Stamp', 'Tag_ID', 'Facility_Code', 'Plaza_Code', 'Lane_Code', 'Vehicle_Speed']

        features = data[data['Columns'].isin(features_list)]
        features = features.drop_duplicates(['Columns'])
        features = features.set_index('Columns')
        features = features.transpose()
        features.insert(0, 'File_Name', filename)
        f = features.reset_index(drop=True)
        # print(features)

        images_df = images_df.append(images,ignore_index=True)
        f_df = f_df.append(f,ignore_index=True)
# print(images_df)
# print(f_df)

myconn = mysql.connector.connect(host="localhost", user="bhavana",
                                 password="Shivani@1805",database="PythonDB")
cur = myconn.cursor()

for i in range(len(images_df)):

    data = (images_df.iloc[i,0], images_df.iloc[i,1], images_df.iloc[i,2], images_df.iloc[i,3])

    cur.execute("insert into PythonDB.Tag_table(File_Name, Images, Back_or_front, File_loc) values(%s,%s,%s,%s)",data)

    print("Records are inserted into tag table")
myconn.commit()

for j in range(len(f_df)):

    data = (f_df.iloc[j,0], pd.Timestamp(f_df.iloc[j,1]), f_df.iloc[j,2], f_df.iloc[j,3], f_df.iloc[j,4], f_df.iloc[j,5], f_df.iloc[j,6])
    cur.execute("insert into PythonDB.feat_table(File_Name, Time_Stamp, Tag_ID, Facility_Code, Plaza_Code, Lane_Code, Vehicle_Speed) "
                "values(%s,%s,%s,%s,%s,%s,%s)",data)

print("Records are inserted into feat table")
myconn.commit()










