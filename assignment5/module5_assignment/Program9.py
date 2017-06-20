import sqlite3 as lite
con = lite.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute('Pragma table_info(Cars)')
    data = cur.fetchall()
    for d in data:
        print d[0], d[1], d[2]