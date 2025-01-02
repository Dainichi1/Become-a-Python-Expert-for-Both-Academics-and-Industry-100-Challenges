import sqlite3

conn = sqlite3.connect('univ.db')

cur = conn.cursor()

'''
rows = cur.execute("select roll,name from Students where city not in ('Delhi')")
rows = cur.execute('select roll,Students.name, Dept.name from Students, Dept where Students.deptno=Dept.deptno')
rows = cur.execute("select city,count(*) from Students group by city")
rows = cur.execute("select city,count(*) from Students group by city having count(*)>2")
'''
rows = cur.execute("select name from Students where city in (select city from Students where name = 'Verma')")

print(rows.fetchall())

cur.close()

conn.close()
