import sqlite3 as lite
con = lite.connect('test.db')
with con:
    con.row_factory = lite.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    for row in rows:
        print "%s %s %s %s" % (row["lat"], row["lon"], row["phone"], row["address"])