import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute("SELECT * FROM user")
data = cur.fetchall()
print(data)

con.close()