import sqlite3

conn = sqlite3.connect('univ.db')

cur = conn.cursor()

# cur.execute('update Dept set name="Chem" where name="Mech"')
# cur.execute('update Students set city="Bhopal" where roll=15')
# cur.execute('delete from  Students where roll=15')
cur.execute('delete from Dept where deptno=40')

conn.commit()

cur.close()

conn.close()
