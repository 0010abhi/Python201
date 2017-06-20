import sqlite3 as lite
import sys
con = lite.connect('test.db')
with con:
 cur = con.cursor()
 cur.execute("SELECT * FROM store")
 for colinfo in cur.description:
   print colinfo