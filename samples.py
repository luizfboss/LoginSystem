import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
  CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
  )
""")

Username1, password1 = "mike213", hashlib.sha256("mikepassword".encode()).hexdigest()
Username2, password2 = "john", hashlib.sha256("ilovecats".encode()).hexdigest()
Username3, password3 = "willsmith", hashlib.sha256("ilikesoccer".encode()).hexdigest()
Username4, password4 = "adamsandler09", hashlib.sha256("bestactor221".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (Username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (Username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (Username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (Username4, password4))

conn.commit()