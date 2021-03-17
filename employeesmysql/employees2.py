import mysql.connector
from employees1 import Employees
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python'
)
myCursor = conn.cursor()
#myCursor.execute('CREATE DATABASE Python')

#myCursor.execute('Show Databases ')
#for x in myCursor:
    # print(x)

#myCursor.execute('Show Tables')
#for x in myCursor:
     #print(x)

#inserting values into table-1
#myCursor.execute("CREATE TABLE crudeoperations(id INT AUTO_INCREMENT PRIMARY KEY , firstname VARCHAR(25),lastname VARCHAR(25),pay INT(20),mail VARCHAR(30))")
#sql = "INSERT INTO CRUDEOPERATIONS (firstname,lastname,pay,mail) values(%s,%s,%s,%s)"
#myCursor.execute(sql, ('rima', 'rafeek', '20000', 'rimarafeek@gmail.com'))

#inserting values into table-2

emp1 = Employees('rima', 'rafeek', 20000, 'rimarafeek@gmail.com')
#sql = "INSERT INTO CRUDEOPERATIONS(firstname,lastname,pay,mail) values(%s,%s,%s,%s)"
#myCursor.execute(sql, (emp1.f, emp1.l, emp1.p, emp1.m))

#inserting values into table-3

#sql ="INSERT INTO CRUDEOPERATIONS(firstname,lastname,pay,mail) values(%s,%s,%s,%s)"
#myCursor.execute(sql,emp1.dict.keys())

#selecting all rows

sql="SELECT * FROM CRUDEOPERATIONS"
myCursor.execute(sql)
for row in myCursor.fetchall():
    print(row)

#updating field values

#sql = "UPDATE CRUDEOPERATIONS set firstname='riya' WHERE lastname='rafeek'"
#myCursor.execute(sql)

#deleting from table

myCursor.execute("DELETE FROM CRUDEOPERATIONS WHERE ID= 4")

#altering table by droping column(index)

sql = "ALTER TABLE CRUDEOPERATIONS DROP COLUMN MAIL"
myCursor.execute(sql)

#altering table by adding column

sql = '''ALTER TABLE CRUDEOPERATIONS
ADD COLUMN mail VARCHAR(20)'''#alter any field
myCursor.execute(sql)

#selecting field values specifying conditions
sql = "SELECT firstname FROM CRUDEOPERATIONS WHERE id=3 AND lastname='rafeek'"
myCursor.execute(sql)
print(myCursor.fetchmany())


conn.commit()
myCursor.close()
conn.close()

