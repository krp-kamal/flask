import sqlite3
db = sqlite3.connect("employee.db")
print("Database connected successfully")

cursor = db.cursor()

cursor.execute("CREATE TABLE emptable(id INTEGER, name TEXT, dept TEXT, city TEXT, salary REAL)")
print("Table created successfully")

db.close()