import sqlite3 as sql
from sqlite3.dbapi2 import Cursor

query = '''
create table student (s_id varchar, s_name varchar, s_age integer)
'''

con = sql.connect('students.sqlite')
print(con.execute(query))

# #Committing changes permanently
# con.commit()

# Inserting single value into database
queryi = "INSERT INTO student VAlUES('18PWCSE1630', 'Mubashir', 23)"
con.execute(queryi)
con.commit()

#Inserting multiple values into database
query = "insert into student values(?, ?, ?)"
data = [
    ('18PWCSE1669', 'Hassan', 22),
    ('18PWCSE1654', 'Jamshid', 21),
    ('18PWCSE1627', 'Qaisar', 22),
    ('18PWMEC4477', 'Zeeshan', 23)
]

con.executemany(query, data)
con.commit()

#Fetching Data from Database
query = "select * from student"
Cursor = con.execute(query)
rows = Cursor.fetchall()

print("Reg No.     Name    Age")
for data in rows:
    print(data[0], data[1], data[2])
