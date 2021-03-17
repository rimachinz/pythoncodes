import sqlite3
from STUDENT import Student
conn=sqlite3.connect('5.db')
myCursor=conn.cursor()

def create_table():
    myCursor.execute('''CREATE TABLE IF NOT EXISTS 'STUDENTDATA'(ID INTEGER
     PRIMARY KEY AUTOINCREMENT NOT NULL,'FIRST' TEXT 'LAST'TEXT,'SUB1'TEXT,'SUB2'TEXT,'SUB3'TEXT )''')
create_table()
stu1=Student('Renu',50,40,60)
stu2=Student('Renil',70,80,90)
stu3=Student('Renush',40,20,60)
stu4=Student('Ayenush',40,20,60)
stu5=Student('Anush',45,27,78)



# myCursor.execute('INSERT INTO STUDENTDATA(ID, FIRST, SUB1, SUB2, SUB3) VALUES(NOT NULL,?,?,?,?)',(stu1.first, stu1.sub1, stu1.sub2, stu1.sub3))
# myCursor.execute('INSERT INTO STUDENTDATA(ID, FIRST, SUB1, SUB2, SUB3) VALUES(NOT NULL,?,?,?,?)',(stu2.first, stu2.sub1, stu2.sub2, stu2.sub3))
# myCursor.execute('INSERT INTO STUDENTDATA(ID, FIRST, SUB1, SUB2, SUB3) VALUES(NOT NULL,?,?,?,?)',(stu3.first, stu3.sub1, stu3.sub3, stu3.sub3))
# myCursor.execute('INSERT INTO STUDENTDATA(ID, FIRST, SUB1, SUB2, SUB3) VALUES(NOT NULL,?,?,?,?)',(stu4.first, stu4.sub1,stu4.sub2, stu4.sub3))
# myCursor.execute('UPDATE  STUDENTDATA SET FIRST=?, SUB1=?, SUB2=?, SUB3=? WHERE id=6',(stu5.first, stu5.sub1, stu5.sub2,stu5.sub3))


# myCursor.execute('INSERT INTO STUDENTDATA(PERCENTAGE) VALUES(?)',(stu1.percentage))

myCursor.execute('SELECT sub1,sub2,sub3 FROM STUDENTDATA' )
for row in myCursor.fetchall():
     print('sum=', Student.total())
# myCursor.execute('ALTER TABLE STUDENTDATA ADD COLUMN PERCENTAGE INTEGER')
# myCursor.execute('UPDATE STUDENTDATA SET PERCENTAGE =? ',(stu1.percentage))

#
# myCursor.execute('SELECT DISTINCT(FIRST) FROM STUDENTDATA ')
# myCursor.execute('SELECT FIRST,COUNT(FIRST) AS COUNT FROM STUDENTDATA GROUP BY FIRST')
# myCursor.execute('SELECT FIRST FROM STUDENTDATA ORDER BY 1 ')
# myCursor.execute('SELECT FIRST,COUNT(FIRST) AS COUNT FROM STUDENTDATA GROUP BY FIRST HAVING COUNT(FIRST)=1')

# myCursor.execute("SELECT FIRST FROM STUDENTDATA WHERE FIRST LIKE'%A%H'")
# for i in myCursor.fetchall():
#     print(i)
# myCursor.execute("SELECT FIRST,COUNT(FIRST) FROM STUDENTDATA WHERE FIRST LIKE'%R%' GROUP BY FIRST")
# for i in myCursor.fetchall():
#     print(i)



conn.commit()
conn.close()


