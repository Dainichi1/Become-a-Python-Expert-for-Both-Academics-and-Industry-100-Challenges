import sqlite3

conn = sqlite3.connect('univ.db')

cur = conn.cursor()

'''
rows = cur.execute('select * from Dept')

print(rows.fetchone())
print(rows.fetchmany(3))
print(rows.fetchall())
'''

'''
rows = cur.execute('select distinct name from Students')
# rows = cur.execute('select distinct name from Students')
# print(rows.fetchall())
allrows = rows.fetchall()
for t in allrows:
    print((t[0]))
'''

'''
rows = cur.execute("select * from Students where city = 'Delhi'")
allrows = rows.fetchall()
for t in allrows:
    print(t)
'''

rows = cur.execute("select * from Students where city = 'Delhi'")
allrows = rows.fetchall()
print('Roll Name City Deptno')
for t in allrows:
    print(t[0], t[1], t[2], t[3])

cur.close()

conn.close()
