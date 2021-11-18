# Group: Diwei Zhang, Yiting Han, Hainan Xiong

import sqlite3
db = sqlite3.connect('pp11.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS candidates")
cursor.execute('''CREATE TABLE candidates (
               id INTEGER PRIMARY KEY NOT NULL, 
               first_name TEXT, 
               last_name TEXT, 
               middle_init TEXT, 
               party TEXT NOT NULL)''')

with open('candidates.txt') as f:
    next(f)
    lines = f.readlines()
for line in lines:
    val = line.split('|')
    cursor.execute('''INSERT INTO candidates(id, first_name, last_name, middle_init, party) VALUES (?, ?, ?, ?, ?)''', (int(val[0]), val[1], val[2],val[3],val[4][:-1]))
db.commit()
cursor.execute("SELECT * FROM candidates")
rows = cursor.fetchall()
print(f'All rows and columns: got {len(rows)} rows')
for row in rows:
    print(row)
db.close()