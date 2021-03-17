import sqlite3

from employee import Employee
conn = sqlite3.connect('empdatabase.db')#connection to sqlite is made
my_Cursor = conn.cursor()#connection taken in a cursor


def create_table():
    my_Cursor.execute('''
    CREATE TABLE IF NOT EXISTS EMPTABLE
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'FIRSTNAME' TEXT, 'LASTNAME' TEXT, 'PAY' INTEGER)
    ''')
create_table()

emp1 = Employee('anu', 's', 10000)
emp2 = Employee('dev', 'p', 20000)

#insert with format()

# my_Cursor.execute('''INSERT INTO EMPTABLE(FIRSTNAME,LASTNAME,PAY)
#     VALUES('{}','{}','{}')'''.format(emp1.f, emp1.l, emp1.p))

#insert by providing values directly

# my_Cursor.execute('''INSERT INTO EMPTABLE(
#     FIRSTNAME,LASTNAME,PAY)VALUES(?,?,?)''', (emp1.f, emp1.l, emp1.p))
#
# #insert using dictionary(secure)
#
# my_Cursor.execute('''INSERT INTO EMPTABLE(FIRSTNAME, LASTNAME, PAY)
#     VALUES(:firstname,:lastname,:pay)''', (emp2.f, emp2.l, emp2.p))
conn.commit()#save changes made in DB

#selecting by specifying condition

# my_Cursor.execute('SELECT * FROM EMPTABLE WHERE FIRSTNAME =:f AND LASTNAME=:l',
 # {'f':'anu','l':'s'})
# print(my_Cursor.fetchall())

#selecting from table

# my_Cursor.execute('SELECT* FROM EMPTABLE')
# print(my_Cursor.fetchmany(2))
# for row in my_Cursor.fetchall():
#     print(row)

#updating field value

# my_Cursor.execute("UPDATE EMPTABLE SET pay=? WHERE firstname= ?", (30000, 'dev'))
# my_Cursor.execute("UPDATE EMPTABLE SET   email= ? WHERE id= ?", (emp1.mail,1))
# my_Cursor.execute("UPDATE EMPTABLE SET   email= ? WHERE id= ?", (emp2.mail,3))
my_Cursor.execute("UPDATE EMPTABLE SET  FULLNAME= ? WHERE id= ?", (emp2.fullname,3))
my_Cursor.execute("UPDATE EMPTABLE SET  FULLNAME= ? WHERE id= ?", (emp1.fullname,2))
my_Cursor.execute("UPDATE EMPTABLE SET  FULLNAME= ? WHERE id= ?", (emp1.fullname,1))

#deleting
# my_Cursor.execute("DELETE FROM EMPTABLE WHERE id= 1")

#deleting table contents

# my_Cursor.execute(" DROP Table emptable ")


#altering table by adding column
# my_Cursor.execute(" ALTER Table emptable ADD EMAIL VARCHAR")
# my_Cursor.execute(" ALTER Table emptable ADD FULLNAME TEXT")

#renaming table
#my_Cursor.execute('ALTER TABLE emptable RENAME TO emptable_old')
#my_Cursor.execute('ALTER TABLE emptable_old RENAME TO emptable')


conn.commit()
my_Cursor.close()
conn.close()