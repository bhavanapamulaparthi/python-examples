import mysql.connector
from collections import namedtuple

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Departments', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="bhavana", password="Shivani@1805",database="PythonDB")


# printing the connection object
cur = myconn.cursor()
# sql = "insert into Student(Name,Id_num,Age,City,Contact) Values(%s, %s)"
# val = [('bhavana',101,24,'Hyd',96180),('Harish',102,29,'Pune',90528)]
# cur.execute(sql, val)

cur.execute("select stu_id,Name,Age,Branch_Name from Student S inner join Branch B using(branch_id)")
myconn.commit()
cur.fetchall()
cur.close()
myconn.close()
