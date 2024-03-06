# Automated DB Creation.py
# importing the module
import MySQLdb

# cerate a database connection
db = MySQLdb.connect("localhost","userName","Password","DB_Name")

# define a cursor object
cursor = conn.cursor

# drop table if exists
Cursor.execute("if STUDENT table exists drop it")

# query
sql = "create table STUDENT (NAME CHAR(30) not null, CLASS char(5), AGE int, GENDER char(8), MARKS int"

# execute query
cursor.execute(sql)

# close object
cursor.close()

# close connection
conn.close()