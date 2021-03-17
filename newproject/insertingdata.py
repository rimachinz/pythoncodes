import MySQLdb as mdb

DBNAME = "dbtest"
DBHOST = "localhost"
DBPASS = ""
DBUSER = "root"

db = mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
cur = db.cursor()
insertquery ='''INSERT INTO Employee(
Name,Age,Email VALUES("Rima","24","rimarafeek@gmail.com")'''
try:
    cur.execute(insertquery)
    db.commit()
    print('done')
except:
    print('failed')
db.close()
