import MySQLdb as mdb

DBNAME = "dbtest"
DBHOST = "localhost"
DBPASS = ""
DBUSER = "root"
try:

    db = mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
    print("connected")
    cur = db.cursor()


    # cur.execute("DROP TABLE IF EXISTS Employee")
    sqlquery ='''CREATE TABLE Employee( 
    Name Char(20) NOT NULL,
    Email CHAR(20),
    Age INT)'''
    cur.execute(sqlquery)
    print('table created')
except mdb.Error as e:
    print("not connected")

