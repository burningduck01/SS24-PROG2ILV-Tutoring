import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS user")
cur.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, name TEXT, role TEXT, dob DATETIME)")

insert = "INSERT INTO user VALUES (:id, :name, :role, :dob)"
cur.execute(insert, {"id": 1, "name": 'root', "role": 'admin', "dob": '01-01-2000'})
cur.execute(insert, {"id": 2, "name": 'max', "role": 'user', "dob": '02-02-2000'})
cur.execute(insert, {"id": 3, "name": 'anne', "role": 'user', "dob": '03-03-2000'})

con.commit()
con.close()