import sqlite3

conn = sqlite3.connect('univ.db')

cur = conn.cursor()
'''
cur.execute('create table Dept(deptno integer primary key, name text)')
cur.execute('create table Students(roll integer primary key, name text, city text, deptno integer, foreign key(deptno) references Dept(deptno))')

cur.execute('insert into Dept values(10, "CSE")')
cur.execute('insert into Dept(name,deptno) values("ECE",20)')

dno = int(input('Enter Deptno'))
dname = input('Enter dname')
cur.execute(f'insert into Dept values({dno},"{dname}")')

cur.execute('INSERT INTO Students VALUES (1, "Ajay", "Delhi", 10)')
cur.execute('INSERT INTO Students VALUES (2, "Vijay", "Kolkata", 10)')
cur.execute('INSERT INTO Students VALUES (3, "Ajay", "Mumbai", 20)')
cur.execute('INSERT INTO Students VALUES (4, "Ramesh", "Delhi", 30)')
cur.execute('INSERT INTO Students VALUES (5, "Suneeta", "Lucknow", 40)')
cur.execute('INSERT INTO Students VALUES (6, "Anita", "Kolkata", 30)')
cur.execute('INSERT INTO Students VALUES (7, "Raj", "Jaipur", 30)')
cur.execute('INSERT INTO Students VALUES (8, "Ali", "Lucknow", 40)')
cur.execute('INSERT INTO Students VALUES (9, "Michael", "Cochin", 10)')
cur.execute('INSERT INTO Students VALUES (10, "Pavan", "Vijayawada", 20)')
cur.execute('INSERT INTO Students VALUES (11, "Suraj", "Hyderabad", 20)')
cur.execute('INSERT INTO Students VALUES (12, "Altaf", "Bangalore", 10)')
cur.execute('INSERT INTO Students VALUES (13, "Ravi", "Indore", 20)')
cur.execute('INSERT INTO Students VALUES (14, "Verma", "Delhi", 10)')
cur.execute('INSERT INTO Students VALUES (15, "Sharma", "Vizag", 10)')

'''

conn.commit()

cur.close()

conn.close()
