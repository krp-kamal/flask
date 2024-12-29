import sqlite3
db=sqlite3.connect("employee.db")
print("database connected successfully")
cursor=db.cursor()
cursor.execute("create table emptable(id int ,name text,dept text,city text,salary text)")

print("table  created")
db.close()

