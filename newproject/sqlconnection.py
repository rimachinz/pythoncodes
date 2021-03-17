import MySQLdb as mdb

DBNAME = "dbtest"
DBHOST = "localhost"
DBPASS = ""
DBUSER = "root"
try:
    db = mdb.connect(DBHOST,DBUSER,DBPASS,DBNAME)
    print("connected")
except mdb.Error as e:
    print("not connected")
